from os import system as sys
import platform

def clear():
    opSys = platform.system()

    if opSys.lower() == "windows":
        return sys('cls')
    elif opSys.lower() == "darwin":
        return sys('clear')
    else:
        print("Unable to recognize operating system")