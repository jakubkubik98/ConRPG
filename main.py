# -----------| ConRPG | -----------
# Made by: Jakub "Hishprung" Kubik
# version: a1.0
# ---------------------------------
import os.path as path
from colorama import Fore

FILES = ["charactersheet.py", "enemies.py", "race.py"]
i = 0
print("DEBUG - File integrity:")
for i in range(len(FILES)):
    checkfile = path.isfile(FILES[i])
    if not checkfile:
        print(Fore.RED + f"{FILES[i]:20s}: NOT FOUND")
    else:
        print(Fore.GREEN + f"{FILES[i]:20s}: OK")

