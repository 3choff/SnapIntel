import requests

import pyaudio
import websocket
import json
import time
import uuid
import numpy as np
import base64


from colorama import Fore
from utils.utils import play_audio_stream
from services.config import deepgram_api_key, elevenlabs_api_key, cartesia_api_key, openai_api_key, XTTS_SPEAKER_NAME, ELEVENLABS_VOICE_ID, CARTESIA_VOICE_ID, DEEPGRAM_MODEL, OPENAI_VOICE, XTTS_LANGUAGE


def generate_speech_deepgram(text):
    
    ENCODING = "aac"
    DEEPGRAM_URL = f"https://api.deepgram.com/v1/speak?model={DEEPGRAM_MODEL}&encoding={ENCODING}"
    
    headers = {
        "Authorization": f"Token {deepgram_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "text": text
    }

    with requests.post(DEEPGRAM_URL, headers=headers, json=data, stream=True) as r:
        audio_stream = r.iter_content(chunk_size=256)
        play_audio_stream(audio_stream)

def generate_speech_openai(text):
    OPENAI_URL = "https://api.openai.com/v1/audio/speech"
    
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "tts-1",
        "input": text,
        "voice": OPENAI_VOICE,
        "response_format": "aac"
    }
    with requests.post(OPENAI_URL, headers=headers, json=data, stream=True) as r:
        audio_stream = r.iter_content(chunk_size=256)
        play_audio_stream(audio_stream)

def generate_speech_fastxttsapi(text):
    FASTXTTSAPI_URL = 'https://localhost:8000'
    
    payload = {
        "text": text,
        "language": XTTS_LANGUAGE,
        "voice": XTTS_SPEAKER_NAME,
        "stream": True,
    }
    with requests.post(FASTXTTSAPI_URL + "/v1/speech", json=payload, verify=False) as r:
        audio_stream = r.iter_content(chunk_size=256)
        play_audio_stream(audio_stream)

def generate_speech_elevenlabs(text):
    ELEVENLABS_URL = f'https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}/stream'
    
    headers = {
        'accept': '*/*',
        'xi-api-key': elevenlabs_api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'voice_settings': {
            'stability': 0.50,
            'similarity_boost': 0.75
        },
        "output_format": "mp3_22050_32" 
    }

    with requests.post(ELEVENLABS_URL, headers=headers, json=data, stream=True) as r:
        audio_stream = r.iter_content(chunk_size=256)
        play_audio_stream(audio_stream)

def generate_speech_cartesia(text):
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), 
                    channels=1,
                    rate=16000,
                    output=True)
    
    url = f"wss://api.cartesia.ai/tts/websocket?api_key={cartesia_api_key}&cartesia_version=2024-06-10"

    data = {
        "context_id": str(uuid.uuid4()),
        "model_id": "upbeat-moon",
        "transcript": text,
        "duration": 180,
        "voice": {
            "mode": "id",
            "id": CARTESIA_VOICE_ID
        },
        "output_format": {
            "container": "raw",
            "encoding": "pcm_s16le",
            "sample_rate": 16000
        }
    }

    ws = websocket.create_connection(url)
    # start_time = time.time()
    ws.send(json.dumps(data))
    done = False
    # first_byte_received = False
    while not done:
        response = ws.recv()
        # if not first_byte_received:
        #     first_byte_time = time.time()  # Record the time when the first byte is received
        #     print(Fore.YELLOW + f"Time to first byte: {(first_byte_time - start_time) * 1000} ms" + Fore.RESET)
        #     first_byte_received = True
        payload = json.loads(response)
        if 'data' in payload:
            binary_data = base64.b64decode(payload['data'])
            data = np.frombuffer(binary_data, dtype='int16').reshape(-1, 1)
            # Write the audio data to the stream
            stream.write(data.tobytes())
        done = payload['done']

    # Close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()