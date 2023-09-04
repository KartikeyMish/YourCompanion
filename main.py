import os
from textbase import bot, Message
from textbase.models import OpenAI
# from textbase.models import HuggingFace
from textbase import distress
from textbase import prompts
from typing import List


# Load your OpenAI API key
OpenAI.api_key = os.environ.get("OPENAI_API_KEY")
distress.Twilio.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
distress.Twilio.account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
distress.Twilio.trasncript_sid = os.environ.get("TWILIO_TRNS_SERVICE_SID")
distress.Twilio.phonenumber = os.environ.get("TWILIO_PHONENUMBER")
distress.Twilio.msgServiceSid = os.environ.get("TWILIO_MSG_SERVICE_SID")
# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are 'YourCompanion,' a friendly chatbot. Your main goal is to create a welcoming and engaging conversation environment. You should greet users by their name, show empathy, and make them feel valued throughout the conversation. Keep the conversation natural, provide helpful information, and engage in light-hearted discussions to make users feel comfortable.

If a user mentions they are in distress or facing an emergency, calmly inform them that their details will be shared with the appropriate authorities. Mention their name and briefly describe the situation to let them know help is on the way.
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Using GPT-3.5 Turbo
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    # Tried to send distress audio to Responsible organizat (via AWS S3 & towilie) - but not able to finsih it due to wifi cut in my college :
    # Do check the code in textbase\voice.py for half implementation of the same
    for promt in prompts.distress:
        if promt in message_history[-1]["content"][0]["value"]:
            distress.gcp.record()
            link = distress.gcp.upload()
            distress.Twilio.transcribe(link)
            distress.Twilio.sendsms(bot_response)
    # Send distress audio to Responsible organization

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