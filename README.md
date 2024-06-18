# SnapIntel
*Voice-to-Voice Assistant for Instant Insights from Screenshots*

SnapIntel is a personal voice-to-voice assistant that provides immediate, actionable insights from the screenshots you decide to share. Whether you're solving an issue or looking for deeper understanding, SnapIntel is here to help.

This project is an open-source initiative that leverages Google Gemini to analyze images and provide responses. Various services are used to transcribe the user queries and generate spoken responses, including the local services [FastWhisperAPI](https://github.com/3choff/FastWhisperAPI) and [FastXttsAPI](https://github.com/3choff/FastXttsAPI).

If you find SnapIntel useful, please consider leaving a star ⭐ or [donate](https://ko-fi.com/3choff).

## Video Demo:


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
- Refer to the [FastWhisperAPI](https://github.com/3choff/FastWhisperAPI) and [FastXttsAPI](https://github.com/3choff/FastXttsAPI) documentation for information on local deployment and requirements of these two services.

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


## Usage

To run the SnapIntel script, use the following command:

```bash
python app.py
```
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
