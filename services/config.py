import os
import importlib

from dotenv import load_dotenv

load_dotenv()

# Define the service choices
TRANSCRIPTION_SERVICE_CHOICE = 'deepgram' # Choices 'deepgram', 'openai', 'groq', 'fastwhisperapi'.
SPEECH_SERVICE_CHOICE = 'deepgram' # Choices 'deepgram', 'openai', 'fastxttsapi, 'elevenlabs', 'cartesia'.
RESPONSE_SERVICE_CHOICE = 'gemini'

# Define the response model name
GEMINI_MODEL = "gemini-1.5-flash-latest" # Choices are "gemini-1.5-flash-latest" or "gemini-1.5-pro-latest"

# Define the transcription services parameters
TRANSCRIPTION_LANGUAGE = "en" # Use ISO 639-1 language codes to choose the language of the transcription or set None to automatically detect the language 
FASTWHISPERAPI_MODEL = "base" # Refer to FastwhisperAPI documentation for the model choices

# Define the speech services parameters
XTTS_SPEAKER_NAME = "Dionisio Schuyler" # Refer to FastxttsAPI documentation for the speaker choices
XTTS_LANGUAGE = "en"
ELEVENLABS_VOICE_ID = "EXAVITQu4vr4xnSDxMaL" # This is the id of Sarah voice, refer to Elevenlabs documentation for the voice choices
CARTESIA_VOICE_ID = "a0e99841-438c-4a64-b679-ae501e7d6091" # This is the id for "Barbershop Man" voice, refer to Cartesia documentation for the voice choices
DEEPGRAM_MODEL = "aura-arcas-en" # Refer to Deepgram documentation for the model choices
OPENAI_VOICE = "nova" # Refer to OpenAI documentation for the voice choices

# Define the API keys from the .env file
deepgram_api_key = os.getenv('DEEPGRAM_API_KEY')
openai_api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
cartesia_api_key = os.getenv('CARTESIA_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')

# Define the available services and their corresponding module paths
TRANSCRIPTION_SERVICES = {
    'deepgram': 'services.transcription_services.transcribe_audio_deepgram',
    'fastwhisperapi': 'services.transcription_services.transcribe_audio_fastwhisperapi',
    'openai': 'services.transcription_services.transcribe_audio_openai',
    'groq': 'services.transcription_services.transcribe_audio_groq',
}

SPEECH_SERVICES = {
    'deepgram': 'services.speech_services.generate_speech_deepgram',
    'fastxttsapi': 'services.speech_services.generate_speech_fastxttsapi',
    'elevenlabs': 'services.speech_services.generate_speech_elevenlabs',
    'cartesia': 'services.speech_services.generate_speech_cartesia',
    'openai': 'services.speech_services.generate_speech_openai',
}

RESPONSE_SERVICES = {
    'gemini': 'services.response_services.generate_response_gemini', 
}

def get_transcription_service():
    return _import_service(TRANSCRIPTION_SERVICES, TRANSCRIPTION_SERVICE_CHOICE)

def get_speech_service():
    return _import_service(SPEECH_SERVICES, SPEECH_SERVICE_CHOICE)

def get_response_service():
    return _import_service(RESPONSE_SERVICES, RESPONSE_SERVICE_CHOICE)

def _import_service(service_dict, service_choice):
    module_path = service_dict.get(service_choice)
    if not module_path:
        raise ValueError(f"Invalid service choice: {service_choice}")
    
    try:
        module_name, func_name = module_path.rsplit('.', 1)
        module = importlib.import_module(module_name)
        return getattr(module, func_name)
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Could not import '{module_path}': {e}")