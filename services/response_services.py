import os
import google.generativeai as genai
import pathlib

def configure_gemini(model_name):
    google_api_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=google_api_key)

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    model = genai.GenerativeModel(
        model_name=model_name,
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    print(f"Configured model: {model_name}")
    return chat_session

def generate_response_gemini(chat_session, message, image_path=None):
    if image_path is not None:
        image_input = {
            'mime_type': 'image/jpeg',
            'data': pathlib.Path(image_path).read_bytes()
        }
        response = chat_session.send_message([message, image_input])
    else:
        response = chat_session.send_message([message])
    print("\n" + response.text)
    return response.text
