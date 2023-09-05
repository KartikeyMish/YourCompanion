import os
from textbase import bot, Message
from textbase.models import OpenAI
from textbase.distress import Twilio, audio
from textbase import prompts
from typing import List


# Load your OpenAI API key
OpenAI.api_key = os.environ.get("OPENAI_API_KEY")
Twilio.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
Twilio.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
Twilio.phonenumber = os.environ.get("TWILIO_PHONENUMBER")
Twilio.msgServiceSid = os.environ.get("TWILIO_MSG_SERVICE_SID")
# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are 'YourCompanion,' a friendly chatbot. Your main goal is to create a 
welcoming and engaging conversation environment. You should greet users by their name, show empathy, 
and make them feel valued throughout the conversation. Keep the conversation natural, provide helpful
information, and engage in light-hearted discussions to make users feel comfortable.

If a user mentions they are in distress or facing an emergency or need help in the emgergency, calmly inform them that their details is being
shared with the appropriate authorities. Mention their name and briefly describe the situation to let them know help is on the way.
"""

distress= """sumary_line: You are an AI system assisting emergency services. 
Below is the transcribed 20-second audio clip in which a person is in distress. 
Your task is to analyze the distress text based on its content and tone, and provide appropriate guidance or instructions accordingly.
[Important] - Make it very short and precise

Return: 
    Audio Transcript (20 seconds):
    [Transcribed text from the audio clip goes here.]

    Distress Text Analysis (Short and Precise):
    [Analyze the distress text, considering both its content and tone. Identify any critical information, emotional state, potential dangers, or specific needs conveyed in the text. Provide guidance or instructions based on your analysis.]

"""


@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Tried to send distress audio to Responsible organizat (via AWS S3 & towilie) - but not able to finsih it due to wifi cut in my college :
    # Do check the code in textbase\voice.py for half implementation of the same
    for promt in prompts.distress:
        if promt in message_history[-1]["content"][0]["value"]:
            voice = audio.record()
            text = OpenAI.transcribe(voice)
            bot_response = OpenAI.generate(system_prompt=distress,text=text)
             # Send distress audio to Responsible organization
            Twilio.sendsms(bot_response)

    # Using GPT-3.5 Turbo
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )
    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }