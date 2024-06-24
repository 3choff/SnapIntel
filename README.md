# SnapIntel
*Voice-to-Voice Assistant for Instant Insights from Screenshots*

SnapIntel is a personal voice-to-voice assistant that provides immediate, actionable insights from the screenshots you decide to share. Whether you're solving an issue or looking for deeper understanding, SnapIntel is here to help.

This project is an open-source initiative that leverages Google Gemini to analyze images and provide responses. Various services are used to transcribe the user queries and generate spoken responses, including the local services [FastWhisperAPI](https://github.com/3choff/FastWhisperAPI) and [FastXttsAPI](https://github.com/3choff/FastXttsAPI).

If you find SnapIntel useful, please consider leaving a star ⭐ or [donate](https://ko-fi.com/3choff).

## Video Demo
[![Video Demo](http://img.youtube.com/vi/pBsyJiFE-C0/0.jpg)](http://www.youtube.com/watch?v=pBsyJiFE-C0 "Video Demo")

## Features
- **Easy and Intuitive Interface:** Use voice-to-voice interactions for a seamless user experience.
- **Privacy-Focused Assistant:** Maintain control over your data; decide what to share with a simple key combination press.
- **Instant Insights:** Receive actionable information quickly from screenshots you choose to analyze.
- **Local Services Integration:** Integrate with FastWhisperAPI and FastXttsAPI for localized query transcription and response vocalization.
- **Chat History:** Records images and interactions within the session, enabling follow-up questions on images and recalling previous queries or responses.
- **Real-Time Session Logging:** Automatically logs session history in a neatly formatted markdown file, accessible in real-time from the local logs folder.
- **Flexibility and Expandability:** Built to adapt and grow with future enhancements and integrations.
- **Transcription Services:** Support OpenAI, Groq, Deepgram, and FastWhisperAPI (Faster Whisper) for efficient transcription of user queries.
- **Speech Services:** Support OpenAI, ElevenLabs, Cartesia, Deepgram, and FastXttsAPI (Coqui) for quick and natural-sounding vocalization of responses.

## Requirements
- Python 3.10 or greater
- [FFmpeg](https://www.ffmpeg.org/download.html). Instructions on how to install it can be found [here](https://www.hostinger.co.uk/tutorials/how-to-install-ffmpeg) 
- [FastWhisperAPI](https://github.com/3choff/FastWhisperAPI) and [FastXttsAPI](https://github.com/3choff/FastXttsAPI) offer local transcription and speech solutions. Their use is **optional**. For information on deployment and requirements of these services, please refer to their respective documentation.

## Dependencies

This project depends on the following libraries:

- pillow
- python-dotenv
- keyboard
- requests
- colorama
- SpeechRecognition
- google.generativeai
- websocket-client
- pyaudio
- numpy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/3choff/SnapIntel.git
    ```

2. Navigate to the project directory:
    ```bash
    cd SnapIntel
    ```

3. Create a new environment:
    ```bash
    python3 -m venv SnapIntel
    ```

4. Activate the virtual environment:

   - **On Unix/Linux/macOS**:
     ```bash
     source SnapIntel/bin/activate
     ```

   - **On Windows**:
     ```bash
     SnapIntel\Scripts\activate
     ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### API keys
SnapIntel uses dotenv to set the API keys. Create a .env file in the root directory with your API keys. Follow the structure of the example.env file as a template.

### Transcription and Speech services
The app supports multiple transcription and speech services right out of the box. You can select from the following options:

Transcription Services:
- Deepgram
- Openai
- Groq
- [FastWhisperAPI](https://github.com/3choff/FastWhisperAPI), a local transcription API server using Faster Whisper.

Speech Services:
- Deepgram
- OpenAI
- ElevenLabs
- Cartesia (EXPERIMENTAL)
- [FastXttsAPI](https://github.com/3choff/FastXttsAPI), a local speech API server using Coqui.

To change the transcription or speech service, simply edit the relevant variables in the Config.py file located in the services folder. The accepted choices are commented next to each variable.

In the same file, you can change other related variables such as voices and language.

## Usage

To run the SnapIntel, use the following command:

```bash
python app.py
```

When the app starts, it will prompt you to either start a new session or resume a previous session stored in the history folder. After making your choice, you can interact with the LLM using these key combinations:

- Press Ctrl+Alt+Space to capture and analyze the screen and invoke the voice assistant.
- Press Ctrl+Space to ask a question without capturing a screenshot or to ask a follow-up question.
- Press ESC to stop speech playback.
- Press Ctrl+C to exit the script.

## Support

If you find this project helpful and would like to support its development, there are several ways you can contribute:
- **Star**: Consider leaving a star ⭐️ to increase the visibility of the project.
- **Support**: Consider [donate](https://ko-fi.com/3choff) to support my work.
- **Contribute**: If you're a developer, feel free to contribute to the project by submitting pull requests or opening issues.
- **Spread the Word**: Share this project with others who might find it useful.

Your support means a lot and helps keep this project going. Thank you for your contribution!

## Acknowledgements

This project is inspired by innovative features showcased by OpenAI in their demo of the upcoming features of ChatGPT, combining voice and vision capabilities to provide assistance and insights. The [Verbi](https://github.com/PromtEngineer/Verbi.git) chatbot project and the [Screen to Voice Tutorial](https://www.youtube.com/watch?v=4olRcVIcBN0&t=743s) of All About AI have significantly influenced this project, forming the foundation for its development. I recommend checking the links if you want to know more.

## License

This project is licensed under the Apache License 2.0.
