# Your Companion - A Personalized AI Chatbot 👋🤖
[![GitHub license](https://img.shields.io/github/license/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/issues)
[![GitHub stars](https://img.shields.io/github/stars/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kartikeymish/yourcompanion)](https://github.com/kartikeymish/yourcompanion/network)

Your Companion is a personalized AI chatbot powered by LLM GPT-3.5 Turbo. It's designed to be your friendly and supportive chat partner, offering a comfortable and conversational experience. Beyond casual conversations, this project also incorporates advanced features for user safety.

## Key Features 🔑

- **Advanced AI Core**: Powered by LLM GPT-3.5 Turbo, Your Companion is a chatbot that engages users in natural and friendly conversations.

- **Prompt Engineering**: Our chatbot is meticulously prompt-engineered to ensure a user-friendly experience, making interactions smooth and enjoyable.

- **Distress Detection**: Your Companion cares about your well-being. It can detect distress signals from user prompts. If distress is detected using `prompts.distress`, the chatbot will take action.

- **Audio Recording**: In distress situations, Your Companion records 10 seconds of audio using the Soundbox module 🎙️, preserving crucial information.

- **Secure Cloud Storage**: The recorded audio is securely stored in a Google Cloud Bucket using the `upload()` method of the distress module, ensuring data privacy and accessibility.

- **Transcription Service**: To provide quick assistance, Your Companion utilizes Twilio API to transcribe the distress audio and forwards the text to responsible authorities via Twilio SMS service 📞.

- **Text-based Framework**: Your Companion's backend is built entirely on a text-based framework, making it highly adaptable and efficient.

## Demo 🚀

- Simply Friendly AI
<br>
<img src="https://github.com/KartikeyMish/YourCompanion/assets/76617485/6f775541-36e3-4867-830e-24f8614f1186" style="height:50%;width:50%"></img>
  <br>

- Sending sms in distress in backed
  ![image](https://github.com/KartikeyMish/YourCompanion/assets/76617485/953e5804-d895-4110-9718-ab15838cfd4b)


## Acquiring API Keys 🔑

Before you can unleash the power of Your Companion, you'll need to acquire the necessary API keys. These keys enable crucial functionalities, so follow these steps to get started:

1. **Google Cloud API Key**: To securely store distress audio recordings, you'll need a Google Cloud API key. You can obtain one by visiting the [Google Cloud Console](https://console.cloud.google.com/), creating a project, and enabling the necessary services. Once you have the API key, make sure to configure it appropriately.

2. **Twilio API Key**: For transcribing distress audio and forwarding it via SMS, you'll need a Twilio API key. Visit the [Twilio Console](https://www.twilio.com/console), create an account, and obtain the API key. Remember to configure it within your application for seamless functionality.

3. **Other API Keys**: Depending on your project's specific requirements, you might need additional API keys like huggingface. Make sure to document and secure all relevant keys to ensure the smooth operation of Your Companion.

By acquiring and properly configuring these API keys, you'll enable Your Companion to provide its full range of features, ensuring a seamless and supportive user experience.


<h2 align="center">
    <p>✨ Textbase is the framework used for building this chatbot using NLP and ML. ✨</p>
</h2>

<p align="center">
  <picture>
    <img alt="Textbase python library" src="assets/logo.svg" width="352" height="59" style="max-width: 100%;">
  </picture>
  <br/>
  <br/>
</p
  <br/>  <br/>
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
![image](https://github.com/KartikeyMish/YourCompanion/assets/76617485/7b51f190-0cdd-4374-ae75-44a288910d65)


### `Other commands have been mentioned in the documentaion website.` [Have a look](https://docs.textbase.ai/usage) 😃!

## Contributions and Support 🤝

We welcome contributions from the open-source community to enhance Your Companion. If you find this project valuable, consider contributing, reporting issues 🐛, or providing feedback 📫. Your support is essential to keep this project thriving.

## License 📜

Your Companion is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.
