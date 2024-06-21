import os
import requests
import json

from colorama import Fore
from services.config import TRANSCRIPTION_LANGUAGE, FASTWHISPERAPI_MODEL, deepgram_api_key, openai_api_key, groq_api_key


def transcribe_audio_deepgram(audio_file_path):
    url = "https://api.deepgram.com/v1/listen?model=nova-2&smart_format=true"
    
    headers = {
        "Authorization": f"Token {deepgram_api_key}",
        "Content-Type": "audio/wav"
    }

    with open(audio_file_path, "rb") as audio_file:
        response = requests.post(url, headers=headers, data=audio_file)
        response.raise_for_status()
        data = response.json()

    transcript = data['results']['channels'][0]['alternatives'][0]['transcript']
    
    print(Fore.BLUE + f"\n{transcript}" + Fore.RESET)

    os.remove(audio_file_path)

    return transcript

def transcribe_audio_fastwhisperapi(audio_file_path, initial_prompt=None, vad_filter=True, min_silence_duration_ms=None, response_format=None, timestamp_granularities=None):
    url = "https://localhost:8000"

    endpoint = url + "/v1/transcriptions"
    files = {
        'file': (audio_file_path, open(audio_file_path, 'rb')),
    }
    data = {
        'model': (None, FASTWHISPERAPI_MODEL),
        'language': (None, TRANSCRIPTION_LANGUAGE),
        'initial_prompt': (None, initial_prompt),
        'vad_filter': (None, vad_filter),
        'min_silence_duration_ms': (None, min_silence_duration_ms),
        'response_format': (None, response_format),
        'timestamp_granularities': (None, timestamp_granularities)
    }
    headers = {
        'Authorization': 'Bearer dummy_api_key',
    }

    response = requests.post(endpoint, files=files, data=data, headers=headers)
    transcript = response.json().get('text', 'No text found in the response.')
    print(Fore.BLUE + f"\n{transcript}" + Fore.RESET)
    return transcript

def transcribe_audio_openai(audio_file_path):
    url = "https://api.openai.com/v1/audio/transcriptions"
    
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
    }
    
    files = {
        'file': (audio_file_path, open(audio_file_path, 'rb')),
    }
    data = {
        "model": "whisper-1",
        "language": TRANSCRIPTION_LANGUAGE
    }
    

    response = requests.post(url, headers=headers, files=files, data=data)
    transcript = response.json().get('text', 'No text found in the response.')
    print(Fore.BLUE + f"\n{transcript}" + Fore.RESET)
    return transcript
def transcribe_audio_groq(audio_file_path):
    url = "https://api.groq.com/openai/v1/audio/transcriptions"
    
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
    }
    
    files = {
        'file': (audio_file_path, open(audio_file_path, 'rb')),
    }
    data = {
        "model": "whisper-large-v3",
        "language": TRANSCRIPTION_LANGUAGE
    }
    

    response = requests.post(url, headers=headers, files=files, data=data)
    transcript = response.json().get('text', 'No text found in the response.')
    print(Fore.BLUE + f"\n{transcript}" + Fore.RESET)
    return transcript