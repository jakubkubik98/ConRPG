attribute = {'LVL': 1, 'NXTLVL': 0, 'EXP': 0, 'LVLUP': 0, 'HP': 0, 'STR': 0, 'DEX': 0,
             'CON': 0, 'AC': 10, 'AB': 0}
whoami = {'Name': "", 'Race': ""}
race = ['Human', 'Elf', 'Dwarf']


# equipment = {"Head": "", "Chest": "", 'Gloves': "", 'Boots': "", 'Weapon': ""}


def printsheet():
    print(f"----CHARACTER---")
    for atttype in whoami.keys():
        print(f"{atttype:6} : {whoami[atttype]} ")
    print(f"---ATTRIBUTES---")
    for atttype in attribute.keys():
        print(f"{atttype:6} : {attribute[atttype]:>5} ")
    # print(f"----EQUIPMENT---") // To be implemented in future
    # for atttype in equipment.keys():
    #     print(f"{atttype:6} : {equipment[atttype]} ")


def createcharacter():
    print()
