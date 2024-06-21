import os
import keyboard
import shutil
import threading

from colorama import Fore

from utils.utils import take_screenshot, record_audio, get_current_datetime
from utils.history import prompt_user_for_session
from utils.log import write_log, update_log
from services.config import get_transcription_service, get_speech_service, GEMINI_MODEL
from services.response_services import configure_gemini, generate_response_gemini, save_chat_history, load_chat_history

transcription_service = get_transcription_service()
speech_service = get_speech_service()
formatted_datetime, readable_datetime = get_current_datetime()

if not os.path.exists('images'):
    os.makedirs('images')
if not os.path.exists('audio'):
    os.makedirs('audio')
if not os.path.exists('logs'):
    os.makedirs('logs')
if not os.path.exists('history'):
    os.makedirs('history')

session_file = prompt_user_for_session(formatted_datetime)
chat_history = load_chat_history(session_file)

# Initialize chat session with the loaded history
chat_session = configure_gemini(GEMINI_MODEL, chat_history)

log_file = f"logs/session_log_{formatted_datetime}.md"
write_log(log_file, chat_history, readable_datetime)

temp_recording_path = 'audio/recording.wav'

flags = {
    "capture_and_analyze": False,
    "ask_question": False
}

keyboard.add_hotkey('ctrl+alt+space', lambda: flags.update({"capture_and_analyze": True}))
keyboard.add_hotkey('ctrl+space', lambda: flags.update({"ask_question": True}))

def handle_capture_and_analyze():
    image_path = take_screenshot()
    record_audio(temp_recording_path)
    question = transcription_service(temp_recording_path)
    text_response = generate_response_gemini(chat_session, question, image_path)
    save_chat_history(chat_session, session_file)
    update_log(question, text_response, log_file, image_path) 
    threading.Thread(target=speech_service, args=(text_response,)).start()

def handle_ask_question():
    record_audio(temp_recording_path)
    follow_up = transcription_service(temp_recording_path)
    follow_up_response = generate_response_gemini(chat_session, follow_up)
    save_chat_history(chat_session, session_file)
    update_log(follow_up, follow_up_response, log_file)
    threading.Thread(target=speech_service, args=(follow_up_response,)).start()

def main():
    try:
        print(Fore.YELLOW + '\nPress "Ctrl+Alt+Space" to capture and analyze the screen, \n"Ctrl+Space" to ask a question with no screenshot or a follow-up question, \n"ESC" to stop speech playback, \n"Ctrl+C" to exit.' + Fore.RESET)
        
        while True:
            if flags["capture_and_analyze"]:
                flags["capture_and_analyze"] = False
                handle_capture_and_analyze()

            if flags["ask_question"]:
                flags["ask_question"] = False
                handle_ask_question()
    
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nScript terminated by user. Exiting..." + Fore.RESET)
        folders_to_delete = ['audio', 'images']
        for folder in folders_to_delete:
            if os.path.exists(folder):
                shutil.rmtree(folder)

if __name__ == "__main__":
    main()
