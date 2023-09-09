# 🔮 Your Companion - Distress Integrated Persona AI Chatbot
[![GitHub license](https://img.shields.io/github/license/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/issues)
[![GitHub stars](https://img.shields.io/github/stars/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/network)

Your Companion is a personalized AI chatbot powered by LLM GPT-3.5 Turbo. It's designed to be your friendly and supportive chat partner, offering a comfortable and conversational experience. Beyond casual conversations, this project also incorporates advanced features for user safety i.e. whenever it detects your are in distress it records yours audio and sends it to the authorities with its thorough analysys.

## Key Features 🔑

- **Advanced AI Core**: Powered by LLM GPT-3.5 Turbo, Your Companion is a chatbot that engages users in natural and friendly conversations.

- **Prompt Engineering**: Our chatbot is meticulously prompt-engineered to ensure a user-friendly experience, making interactions smooth and enjoyable.

- **Distress Detection**: Your Companion cares about your well-being. It can detect distress signals from user prompts. If distress is detected using `prompts.distress`, the chatbot will take action.

- **Audio Recording**: In distress situations, Your Companion records 15 seconds of audio using the Soundbox module 🎙️, safeguarding  crucial information.

- **Accurate Transcription**: Your Companion employs OpenAI's `audio` module, leveraging the `whisper-1` model for precise, multilingual distress audio-to-text transcription, ensuring reliability and accessibility.

- **Rapid Alert System**: Your Companion harnesses the power of the **Twilio API** to swiftly notify authorities. It sends the transcribed text, enriched with detailed analysis from `GPT-3.5-turbo`, via Twilio SMS service 📞 for prompt action.

- **Text-based Framework**: Your Companion's backend is built entirely on a text-based framework, making it highly adaptable and efficient.

## Demo 🚀

[Go See the Detailed Demo](https://drive.google.com/drive/folders/1_F-yX2cvbCoHjiWe9s1rydHM4xMc4wXx?usp=drive_link)


While interacting with Simply Friendly AI, you have access to a powerful Distress Alert System. Here's how it works:

<img src="https://github.com/KartikeyMish/YourCompanion/assets/76617485/54b493e9-fe11-4618-8382-dc9458b2c794"></img>

#### In Case of Distress:

If you ever find yourself in a distressing situation, our system is designed to assist you. When you activate the distress feature, an SMS alert will be sent discreetly in the background.

![SMS in Distress](https://github.com/KartikeyMish/YourCompanion/assets/76617485/c367b439-cebd-435d-9b1a-544d7e3a2772)

#### Message to Authorities:

Here's a glimpse of the message that will be sent to the relevant authorities once your audio is recorded and distress is confirmed:

<img src="https://github.com/KartikeyMish/YourCompanion/assets/76617485/a990c17f-cad7-4f60-a864-db435cf82c7f" style="height: 50%; width: 50%;"></img>

Your safety is our priority. With this system in place, you can always feel secure, knowing that help is just a click away.


## Before Getting Started: Acquiring API Keys 🔑

To begin with Your Companion, you'll need to acquire the necessary API keys. These keys are essential for enabling crucial functionalities in the chatbot. Here's what you need:

1. **OpenAI API Key**: This key is required for using the OpenAI service, which powers the chatbot's core functionality. You can obtain an OpenAI API key by visiting the [OpenAI platform](https://www.openai.com) and following their authentication process.

2. **Twilio API Key**: The Twilio API key is necessary for SMS notifications and communications. To obtain one, create an account on the [Twilio platform](https://www.twilio.com) and follow their authentication process.

Before diving into any development or interaction, make sure to have these API keys ready and properly configured in your project. They will ensure that Your Companion functions seamlessly and efficiently.



<h2 align="center">
    <p>✨ Textbase is the framework used for building this chatbot using NLP and ML. ✨</p>
</h2>

<p align="center">
  <picture>
    <img alt="Textbase python library" src="assets/logo.svg" width="352" height="59" style="max-width: 100%;">
  </picture>
  <br/>
</p
  <br/> 
  
## Installation
Make sure you have `python version >=3.9.0`, it's always good to follow the [docs](https://docs.textbase.ai/get-started/installation) 👈🏻
### 1. Through pip
```bash
pip install textbase-client
```

### 2. Local installation
Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

For proper details see [here]()

```bash
git clone https://github.com/kartiikeyish/yourcomapnion
cd textbase
poetry shell
poetry install
```

### 3. Install all the requiremnts 

```bash
pip install -r requiremetns.txt
```

## Start development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.

Run the following command:
- if installed locally
    ```bash
    poetry run python textbase/textbase_cli.py test
    ```
- if installed through pip
    ```bash
    textbase-client test
    ```
Response:
```bash
Path to the main.py file: examples/openai-bot/main.py # You can create a main.py by yourself and add that path here. NOTE: The path should not be in quotes
```
Now go to the link in blue color which is shown on the CLI and you will be able to chat with your bot!
![image](https://github.com/KartikeyMish/YourCompanion/assets/76617485/7d375d1d-72d1-4970-8176-cf0a18b75696)

> `Other commands have been mentioned in the documentaion website.` [Have a look](https://docs.textbase.ai/usage) 😃!
<br>

## Sponsoring💰🤝 and Supporting 🙌👨‍💻 Your Companion 

Your Companion is a project driven by innovation and community support. We invite individuals and organizations to sponsor and support our efforts in the following ways:

1. **API Key Sponsorship** 🗝️: The API keys required for Openai and Twilio services are essential for the continued operation of Your Companion. As these services may involve ongoing costs, sponsoring for API keys service can help us keep the project accessible to users. Your sponsorship will ensure that users can continue to benefit from Your Companion's services without interruptions.

2. **Advanced Feature Development** 🌟: Your support enables us to implement advanced features and improvements to enhance the capabilities of Your Companion. Whether it's adding new conversational skills or improving distress detection algorithms, your contributions will directly impact the quality of the chatbot.

3. **Open Source Contributions** 🤝: If you're a developer or part of an organization with technical expertise, consider contributing to the project directly. We welcome open-source contributions that help improve Your Companion and make it even more valuable to users.

By sponsoring or supporting Your Companion, you contribute to the development of a compassionate and innovative AI chatbot that can positively impact users' lives. To discuss sponsorship opportunities or get involved, please visit [my sponser dashboard](https://github.com/sponsors/KartikeyMish)

We sincerely appreciate your support in making Your Companion a helpful and supportive tool for users around the world.

## License 📜

Your Companion is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.
