# -----------| ConRPG | -----------
# Made by: Jakub "Hishprung" Kubik
# version: a1.0
# ---------------------------------
import os.path as path
import charactersheet
import time
from colorama import Fore
from colorama import init

init(autoreset=True)

FILES = ["charactersheet.py", "enemies.py", "race.py, conversations.py"]


def menu():
    makechoice = 0
    print("\n" * 10)
    if charactersheet.whoami['Name'] == "":
        charactersheet.createcharacter()
    print("""1: Find enemy!
2: Character sheet
e: Exit""")
    while makechoice != "e":
        if makechoice == "1":
            # Find Enemy function
            break
        if makechoice == "2":
            charactersheet.printsheet()
            print("")
            menu()
        if makechoice == "e":
            break  # Exit
        makechoice = input()


print("DEBUG - File integrity:")
for i in range(len(FILES)):
    checkfile = path.isfile(FILES[i])
    if not checkfile:
        print(Fore.RED + f"{FILES[i]:20s}: NOT FOUND")
    else:
        print(Fore.GREEN + f"{FILES[i]:20s}: OK")

time.sleep(3)
menu()
