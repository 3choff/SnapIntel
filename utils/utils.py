
import subprocess
import keyboard
import speech_recognition as sr
import base64

from PIL import ImageGrab
from colorama import Fore
from datetime import datetime
from datetime import datetime

stop_playback = False

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def update_markdown_log(question, response, log_file, image_path=None):
    with open(log_file, "a", encoding="utf-8") as f:
        if image_path:
            image_base64 = image_to_base64(image_path)
            f.write(f"### Captured Image:\n![Image](data:image/jpeg;base64,{image_base64})\n")
        f.write(f"### Question:\n{question}\n")
        f.write(f"### Response:\n{response}\n\n")

def get_current_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
    readable_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime, readable_datetime

def take_screenshot():
    screenshot = ImageGrab.grab()

    # Uncomment the resolution you want to resize the image to
    screenshot = screenshot.resize((1024, 576))
    # screenshot = screenshot.resize((896, 504))
    # screenshot = screenshot.resize((768, 432))
    # screenshot = screenshot.resize((512, 512))
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = f"images/screenshot_{timestamp}.jpg"
    
    screenshot.save(image_path, 'JPEG')
    print(Fore.YELLOW + "\nScreenshot acquired" + Fore.RESET)
    return image_path

def play_sound(file_path):
    subprocess.call(['ffplay', '-nodisp', '-autoexit', file_path], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

def play_audio_stream(audio_stream):
    global stop_playback
    stop_playback = False
    
    ffplay_cmd = ['ffplay', '-probesize', '256', '-autoexit', '-', "-nodisp"]
    ffplay_proc = subprocess.Popen(
        ffplay_cmd, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    def stop_audio():
        global stop_playback
        stop_playback = True

    keyboard.add_hotkey('esc', stop_audio)

    try:
        for chunk in audio_stream:
            if stop_playback:
                print(Fore.YELLOW + f"\nPlayback stopped by user." + Fore.RESET)
                break
            ffplay_proc.stdin.write(chunk)
            # print("Received and played a chunk")
    except Exception as e:
        print(Fore.RED + f"\nAn error occurred: {e}" + Fore.RESET)
    finally:
        if ffplay_proc.stdin:
            ffplay_proc.stdin.close()
        ffplay_proc.wait()
        # Remove the hotkey when done to avoid side effects
        keyboard.remove_hotkey('esc')

def record_audio(file_path, energy_threshold=2000, pause_threshold=1.0):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = energy_threshold
    recognizer.pause_threshold = pause_threshold

    with sr.Microphone() as source:
        # print(Fore.YELLOW + f"\nRecording started" + Fore.RESET)
        play_sound("./assets/beep.mp3")
        audio_data = recognizer.listen(source)
        # print(Fore.YELLOW + f"\nRecording complete" + Fore.RESET)
        play_sound("./assets/clack.mp3")
        with open(file_path, "wb") as audio_file:
            audio_file.write(audio_data.get_wav_data())