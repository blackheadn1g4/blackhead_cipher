import json
import colorama
from colorama import Fore
from pystyle import *

intro = '''
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░██╗███████╗░█████╗░██████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔════╝██╔══██╗██╔══██╗
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░███████║█████╗░░███████║██║░░██║
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╔══██║██╔══╝░░██╔══██║██║░░██║
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗██║░░██║███████╗██║░░██║██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░

          ░█████╗░██╗░░░██╗██████╗░██╗░░██╗███████╗██████╗░
          ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗
          ██║░░╚═╝░╚████╔╝░██████╔╝███████║█████╗░░██████╔╝
          ██║░░██╗░░╚██╔╝░░██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
          ╚█████╔╝░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║
          ░╚════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                          Press Enter >>>
'''

Anime.Fade(
    Center.Center(intro),
    Colors.green_to_red,
    Colorate.Vertical,
    interval=0.035,
    enter=True,
)

print(f'''{Fore.LIGHTGREEN_EX}

██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░██╗███████╗░█████╗░██████╗░
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░░██║██╔════╝██╔══██╗██╔══██╗
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░███████║█████╗░░███████║██║░░██║
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╔══██║██╔══╝░░██╔══██║██║░░██║
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗██║░░██║███████╗██║░░██║██████╔╝
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░

          ░█████╗░██╗░░░██╗██████╗░██╗░░██╗███████╗██████╗░
          ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗
          ██║░░╚═╝░╚████╔╝░██████╔╝███████║█████╗░░██████╔╝
          ██║░░██╗░░╚██╔╝░░██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
          ╚█████╔╝░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║
          ░╚════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

''')

def crypt(task, sentence, keys) -> str:
    result = ""
    for letter in sentence:
        for key in keys:
            if task.lower() == "encrypt":
                if letter == key:
                    result += keys[key]
            elif task.lower() == "decrypt":
                if letter == keys[key]:
                    result += key
            else:
                raise ValueError("Invalid encryption assigned")

    return result


def main():
    with open("keys.json", "r") as f:
        keys = json.load(f)

    active = True

    while active:
        print("[1] Encrypting text.")
        print("[2] Decrypting text.")

        try:
            usr_input = int(input(">>> "))
        except ValueError:
            continue

        if usr_input == 1:
            sentence = str(input("\nEnter sentence >>> "))
            encryption = crypt("encrypt", sentence, keys)

            print("\n========================ENCRYPTED TEXT===========================\n")
            print(encryption)
            print("\n=================================================================\n")

        elif usr_input == 2:
            sentence = str(input("\n Enter sentence >>> "))
            decryption = crypt("decrypt", sentence, keys)

            print("\n========================DECRYPTED TEXT===========================\n")
            print(decryption)
            print("\n=================================================================\n")

        exit_stay = str(input("If you want to exit, type 'x'. If not and you would like to continue, press 'Enter' key >>> "))

        if exit_stay == "x":
            active = False


if __name__ == "__main__":
    main()
