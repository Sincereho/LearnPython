#I want to reproduce the effect of Uplay Fools' Day eggs in 2018
from sys import exit
carbin_key = False


def forest_site():
    global carbin_key
    print("")
    print("One your right, you see a lake. The fog hovering above it.")
    print("On you left, you see the silhouette of a cabin.")

    while True:
        print("")
        print("What do you do?")
        print("go to cabin")
        print("go to lake")

        next = input("> ")
        print("")

        if next == "go to cabin" and carbin_key:
            print("Door unlocked")
            cabin_site()
        elif next == "go to cabin" and not carbin_key:
            print("The door seems to be locked.")
            print("You are in the forest.")
        elif next == "go to lake":
            lake_site()
        else:
            print("I got no idea what that means.")
            print("")


def cabin_site():
    print("")
    print("The carbin is cozy and warm, it appears lived-in")
    print("There is nothing but a dest in it.")
    print("On the dest, there is a note.")
    print("")

    while True:
        print("What do you do?")
        print("go to forest")
        print("take note")

        next = input("> ")
        print("")

        if next == "go to forest":
            forest_site()
        elif next == "take note":
            note_site()
        else:
            print("I got no idea what that means.")
            print("")


def note_site():
    print("")
    print("Now you know the way out.")
    print("Congratulations! You win!")
    exit(0)


def lake_site():
    global carbin_key
    print("")
    print(
        "The lake is vast and reaches beyond the horizon.It is completely still."
    )
    print("One the left, there is a wooden bridge. It looks old.")
    print("You cannot see clearly, the fog obscures your vision.")
    print("There you hear a distant voice, but you can't make out the words.")

    while True:
        print("")
        print("What do you do?")
        print("go to bridge")
        print("go to forest")
        if not carbin_key:
            print("peer into the lake")

        next = input("> ")
        print("")

        if next == "go to bridge":
            bridge_site()
        elif next == "go to forest":
            forest_site()
        elif next == "peer into the lake" and not carbin_key:
            carbin_key = True
            print("Key retrieved.")
        elif next == "peer into the lake" and carbin_key:
            print("Do not need to do that")
        else:
            print("I got no idea what that means.")
            print("")


def bridge_site():
    print("")
    print("The bridge is broken.")

    while True:
        print("")
        print("What do you do?")
        print("go to lake")

        next = input("> ")
        print("")

        if next == "go to lake":
            lake_site()
        else:
            print("I got no idea what that means.")
            print("")


def start():
    global carbin_key
    carbin_key = False
    print("You are stranded in the middle of a forest at dusk.")
    print(
        "The forest is thick, you are surrounded by tall pines that stretch into the sky."
    )
    print("It is cold and foggy. you don't know how you ended up here.")
    print(
        "The last thing you remember is a thunderous noise and blinding light."
    )
    print(
        "You feel extremely weak, your body feels heavy and is covered in burises."
    )
    forest_site()


start()
