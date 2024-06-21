import os
from colorama import Fore

def prompt_user_for_session(formatted_datetime):
    
    response = input(Fore.YELLOW + "\nDo you want to load a previous conversation? (y/n): " + Fore.RESET).strip().lower()
    if response == 'y':
        available_files = [f for f in os.listdir('history') if f.endswith('.pkl')]
        if not available_files:
            print(Fore.YELLOW + "\nNo previous sessions found. Starting a new conversation." + Fore.RESET)
            return f'history/session_history_{formatted_datetime}.pkl'
        print("Available sessions:")
        for idx, file in enumerate(available_files):
            print(f"{idx + 1}. {file}")
        while True:
            try:
                file_choice = int(input(Fore.YELLOW + "\nEnter the number of the session you want to resume: " + Fore.RESET)) - 1
                if 0 <= file_choice < len(available_files):
                    return os.path.join('history', available_files[file_choice])
                else:
                    print(Fore.RED + "Invalid choice. Please try again." + Fore.RESET)
            except ValueError:
                print(Fore.YELLOW + "Invalid input. Please enter a number." + Fore.RESET)
    else:
        return f'history/session_{formatted_datetime}.pkl'