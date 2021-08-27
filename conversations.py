from colorama import Fore
from colorama import init
import time
import charactersheet

init(autoreset=True)


def newcharacterconv():
    print(f"""Welcome new adventurer! 
I welcome you in this tavern! Im Bob, and been running this place for 20 years already.""")
    time.sleep(1)
    while charactersheet.whoami["Name"] == "":
        print(f"How do people call you?")
        charactersheet.whoami["Name"] = input(f"{Fore.CYAN}Please put your name here: ")
        if charactersheet.whoami["Name"] == "":
            print(f"{Fore.RED}Please write correct name. Try again.")
    time.sleep(1)
    print(f"{Fore.LIGHTMAGENTA_EX}{charactersheet.whoami['Name']}" + f"?")
    time.sleep(1)
    print(f"Not the name I've heard before... But dont worry, im sure in time you'll be known around here, maybe even "
          f"around this kingdom")
    time.sleep(1)
    print(f"...if you'll be able to live the day of course. Say, looking at you i can tell you're...")
    time.sleep(1)
    while charactersheet.whoami["Race"] != "Human" and charactersheet.whoami["Race"] != "Elf" and charactersheet.whoami[
            "Race"] != "Dwarf" and charactersheet.whoami["Race"] == "":
        print(f"What race do you pick. Awaitable options (case sensitive): ")
        print(charactersheet.race[0], charactersheet.race[1], charactersheet.race[2])
        charactersheet.whoami["Race"] = input(f"{Fore.CYAN}Please put your race here: ")
        if charactersheet.whoami["Race"] != "Human" and charactersheet.whoami["Race"] != "Elf" and charactersheet.whoami[
            "Race"] != "Dwarf" and charactersheet.whoami["Race"] != "":
            print(f"{Fore.RED}Please write correct race. Try again.")
    time.sleep(1)
    print(f"{Fore.LIGHTMAGENTA_EX}{charactersheet.whoami['Race']}")
    print(f"...im sure you'll find many of your kin then.")
    time.sleep(1)


newcharacterconv()
