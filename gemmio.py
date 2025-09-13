# Gemmio - Gemini in your terminal
# Made with ❤️ by Soham | Open Source

import google.generativeai as genai
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# ========= CONFIG =========
# ⚠️ Sample public API key (NOT valid) — replace it with your own Gemini API key
API_KEY = "AIzaSyAvW4wShWmzlLtExZnyRDCkPTg2-bfdhlc"
MODEL_NAME = "gemini-1.5-flash"
# ==========================

# ASCII Logo
def show_logo():
    logo = f"""
{Fore.RED}··········································
{Fore.RED}····{Fore.GREEN}███████{Fore.RED}····{Fore.GREEN}███{Fore.RED}····{Fore.GREEN}███{Fore.RED}····
{Fore.RED}····{Fore.GREEN}██{Fore.RED}······{Fore.GREEN}██{Fore.RED}···{Fore.GREEN}██{Fore.RED}··{Fore.GREEN}██{Fore.RED}···{Fore.GREEN}██{Fore.RED}··
{Fore.RED}····{Fore.GREEN}███████{Fore.RED}···{Fore.GREEN}██{Fore.RED}····{Fore.GREEN}██{Fore.RED}···{Fore.GREEN}██{Fore.RED}··
{Fore.RED}····{Fore.GREEN}██{Fore.RED}······{Fore.GREEN}██{Fore.RED}···{Fore.GREEN}██{Fore.RED}···{Fore.GREEN}██{Fore.RED}···{Fore.GREEN}██{Fore.RED}··
{Fore.RED}····{Fore.GREEN}███████{Fore.RED}····{Fore.GREEN}███{Fore.RED}····{Fore.GREEN}███{Fore.RED}····
{Fore.RED}··········································
    """
    print(logo)
    print(f"{Fore.GREEN}Welcome to Gemmio! Use Gemini AI right in your terminal.\n")


def configure_gemini():
    if not API_KEY or "AIza" not in API_KEY:
        print(f"{Fore.RED}[ERROR] Please replace the sample API key with your own in gemmio.py")
        exit(1)
    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel(MODEL_NAME)


def run_chat(model):
    print(f"{Fore.RED}Type {Fore.GREEN}'exit'{Fore.RED} to quit.\n")
    chat = model.start_chat(history=[])
    while True:
        user_input = input(f"{Fore.GREEN}You{Fore.RED} >>> {Style.RESET_ALL}")
        if user_input.lower() in ["exit", "quit"]:
            print(f"{Fore.RED}Goodbye from Gemmio! Stay red & green. 🌱🩸")
            break
        try:
            response = chat.send_message(user_input)
            print(f"{Fore.RED}Gemmio{Fore.GREEN} >>> {Style.RESET_ALL}{response.text}\n")
        except Exception as e:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {e}")
            break


if __name__ == "__main__":
    show_logo()
    model = configure_gemini()
    run_chat(model)
