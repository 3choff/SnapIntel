import importlib

# Define the service choices
TRANSCRIPTION_SERVICE_CHOICE = 'deepgram' # Choices 'deepgram', 'openai', 'groq', 'fastwhisperapi'.
SPEECH_SERVICE_CHOICE = 'deepgram' # Choices 'deepgram', 'openai', 'fastxttsapi, 'elevenlabs', 'cartesia'.
RESPONSE_SERVICE_CHOICE = 'gemini'

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

