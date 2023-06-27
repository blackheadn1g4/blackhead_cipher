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

          ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
          ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
          ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
          ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
          ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
          ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
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

          ░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
          ██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
          ██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
          ██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
          ╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
          ░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

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
    keys = {
        "a": "e",
        "b": "a",
        "c": "m",
        "d": "c",
        "e": "d",
        "f": "b",
        "g": "h",
        "h": "i",
        "i": "f",
        "j": "o",
        "k": "g",
        "l": "r",
        "m": "j",
        "n": "l",
        "o": "n",
        "p": "s",
        "q": "q",
        "r": "w",
        "s": "t",
        "t": "v",
        "u": "u",
        "v": "z",
        "w": "k",
        "x": "p",
        "y": "x",
        "z": "y",
        "A": "Y",
        "B": "X",
        "C": "P",
        "D": "K",
        "E": "Z",
        "F": "U",
        "G": "V",
        "H": "T",
        "I": "W",
        "J": "Q",
        "K": "S",
        "L": "N",
        "M": "L",
        "N": "J",
        "O": "R",
        "P": "G",
        "Q": "O",
        "R": "F",
        "S": "I",
        "T": "H",
        "U": "B",
        "V": "D",
        "W": "C",
        "X": "M",
        "Y": "A",
        "Z": "E",
        "1": "8",
        "2": "0",
        "3": "7",
        "4": "9",
        "5": "2",
        "6": "4",
        "7": "5",
        "8": "3",
        "9": "1",
        "0": "6",
        "-": "~",
        "+": "¬",
        "=": "`",
        " ": "£",
        ",": ">",
        ";": "<",
        ":": "?",
        "'": "/",
        "%": "}",
        "#": "{",
        "!": "]",
        "$": "[",
        "(": "_",
        ")": "*",
        "&": "&",
        "*": ")",
        "_": "(",
        "[": "$",
        "]": "!",
        "{": "#",
        "}": "%",
        "/": "'",
        "?": ":",
        "<": ";",
        ">": ",",
        "£": " ",
        "`": "=",
        "¬": "+",
        "~": "-"
    }

    active = True

    while active:
        print(f"{Fore.WHITE}[{Fore.MAGENTA}1{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Encrypting text.")
        print(f"{Fore.WHITE}[{Fore.MAGENTA}2{Fore.WHITE}] {Fore.LIGHTGREEN_EX}Decrypting text.")
        print("")
        
        try:
            usr_input = int(input(f"{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] "))
        except ValueError:
            continue

        if usr_input == 1:
            print(f"\n{Fore.LIGHTGREEN_EX}Enter sentence!")
            sentence = str(input(f"{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] "))
            encryption = crypt("encrypt", sentence, keys)

            print(f"\n{Fore.LIGHTGREEN_EX}======================== {Fore.MAGENTA}ENCRYPTED TEXT {Fore.LIGHTGREEN_EX}===========================\n")
            print(encryption)
            print("\n===================================================================\n")

        elif usr_input == 2:
            print(f"\n{Fore.LIGHTGREEN_EX}Enter sentence!")
            sentence = str(input(f"{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] "))
            decryption = crypt("decrypt", sentence, keys)

            print(f"\n{Fore.LIGHTGREEN_EX}======================== {Fore.MAGENTA}DECRYPTED TEXT {Fore.LIGHTGREEN_EX}===========================\n")
            print(decryption)
            print("\n===================================================================\n")
            print("")
            print(f"{Fore.LIGHTGREEN_EX}If you want to {Fore.RED}exit{Fore.LIGHTGREEN_EX}, {Fore.LIGHTGREEN_EX}type {Fore.LIGHTGREEN_EX}'{Fore.MAGENTA}x{Fore.LIGHTGREEN_EX}'. {Fore.LIGHTGREEN_EX}If not and you would like to continue, press {Fore.LIGHTGREEN_EX}'{Fore.MAGENTA}Enter{Fore.LIGHTGREEN_EX}' {Fore.LIGHTGREEN_EX}key.")     
            print("")
        exit_stay = str(input(f"{Fore.WHITE}[{Fore.MAGENTA}>>>{Fore.WHITE}] "))

        if exit_stay == "x":
            active = False


if __name__ == "__main__":
    main()
