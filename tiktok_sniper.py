import requests
import time
from colorama import Fore, Style, init
from pyfiglet import Figlet
import random
import string

init(autoreset=True)

BANNER_TEXT = "Kyn TikTok Sniper"
AUTHOR = "Created by Kyn"
MENU_COLOR = Fore.RED
DELAY = 2.5
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
OUTPUT_FILE = "valid.txt"

def print_banner():
    fig = Figlet(font='slant')
    print(MENU_COLOR + fig.renderText(BANNER_TEXT))
    print(MENU_COLOR + AUTHOR + "\n" + "-"*50 + "\n")

def check_username(username):
    try:
        r = requests.get(f"https://www.tiktok.com/@{username}", headers=HEADERS, timeout=10)
        return "Couldn't find this account" in r.text
    except:
        return False

def generate_pattern(choice, custom_pattern=None):
    letters = string.ascii_uppercase
    numbers = string.digits

    if choice == "1":  
        return random.choice(letters) + "_" + "".join(random.choices(letters, k=3))
    elif choice == "2":  
        return "".join(random.choices(letters, k=2)) + "_" + "".join(random.choices(letters, k=2))
    elif choice == "3":  
        return "".join(random.choices(letters, k=3)) + "_" + random.choice(letters)
    elif choice == "4":  
        return random.choice(numbers) + "_" + random.choice(letters) + random.choice(numbers) + random.choice(letters)
    elif choice == "5":  
        return random.choice(numbers) + random.choice(letters) + "_" + random.choice(numbers) + random.choice(letters)
    elif choice == "6":  
        return random.choice(numbers) + random.choice(letters) + random.choice(numbers) + "_" + random.choice(letters)
    elif choice == "7":  
        return random.choice(letters) + random.choice(numbers) + random.choice(letters) + random.choice(numbers) + random.choice(letters)
    elif choice == "8":  # Custom
        result = ""
        for char in custom_pattern:
            if char.upper() == "X":
                result += random.choice(letters)
            elif char == "1":
                result += random.choice(numbers)
            else:
                result += char
        return result
    return None

def main_menu():
    print(MENU_COLOR + "Choose a pattern:\n")
    print(MENU_COLOR + "1. X_XXX  (e.g. C_RAQ, W_VVL)")
    print(MENU_COLOR + "2. XX_XX  (e.g. BH_ZZ, SU_XQ)")
    print(MENU_COLOR + "3. XXX_X  (e.g. HSD_Y, XZK_E)")
    print(MENU_COLOR + "4. 1_X2X  (e.g. P_M5R, 9_J9L)")
    print(MENU_COLOR + "5. 1X_2X  (e.g. GG_1F, WH_6D)")
    print(MENU_COLOR + "6. 1X2_X  (e.g. 8F7_P, RZ4_Z)")
    print(MENU_COLOR + "7. X1X2X  (e.g. EH3QL, QE4PA)")
    print(MENU_COLOR + "8. Custom pattern (e.g., LLDLD → MQ9F5, VZ3P0)")
    print(MENU_COLOR + "9. Load from .txt file\n")

    return input(MENU_COLOR + "Enter your choice: ").strip()

def main():
    while True:
        print_banner()
        choice = main_menu()
        usernames = []

        if choice == "9":
            filename = input("Enter the filename: ").strip()
            with open(filename, "r", encoding="utf-8") as f:
                usernames = [u.strip() for u in f if u.strip()]
        else:
            count = int(input("How many usernames to generate? ").strip())
            custom_pattern = None
            if choice == "8":  # Ask custom pattern only once
                custom_pattern = input("Enter your custom pattern (X=letter, 1=number, _=underscore): ").strip()

            for _ in range(count):
                usernames.append(generate_pattern(choice, custom_pattern))

        with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
            total = len(usernames)
            checked = 0
            for user in usernames:
                available = check_username(user)
                checked += 1
                if available:
                    print(Fore.GREEN + f"[{checked}/{total}] {user} AVAILABLE")
                    out.write(user + "\n")
                else:
                    print(Fore.RED + f"[{checked}/{total}] {user} TAKEN")
                time.sleep(DELAY)

        print(Fore.YELLOW + f"\n✅ Done! Results saved to {OUTPUT_FILE}\n")
        again = input("Do you want to run the menu again? (y/n): ").strip().lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()
