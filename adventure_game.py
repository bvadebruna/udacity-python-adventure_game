import time
# print("Hello")
# time.sleep(2)
# print("world!")

import random


def print_delay(output_text):
    print(output_text)
    time.sleep(2)


def welcome_text(item, option):
    print_delay("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
    print_delay("Rumor has it that a " + option + " is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    print_delay("In front of you is a house.\n")
    print_delay("To your right is a dark cave.\n")
    print_delay("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


def cave(item, option):
    if "sward" in item:
        print_delay("\nYou peer cautiously into the cave.")
        print_delay("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_delay("\nYou walk back to the field.\n")
    else:
        print_delay("\nYou peer cautiously into the cave.")
        print_delay("\nIt turns out to be only a very small cave.")
        print_delay("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_delay("\nYou have found the magical Sword of Ogoroth!")
        print_delay("\nYou discard your silly old dagger and take "
                    "the sword with you.")
        print_delay("\nYou walk back out to the field.\n")
        item.append("sward")
    cave_or_house(item, option)


def house(item, option):
    print_delay("\nYou approach the door of the house.")
    print_delay("\nYou are about to knock when the door "
                "opens and out steps a " + option + ".")
    print_delay("\nEep! This is the " + option + "'s house!")
    print_delay("\nThe " + option + " attacks you!\n")
    if "sward" not in item:
        print_delay("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        choice = input("Would you like to (1) fight or (2) run away?")
        if choice == "1":
            if "sward" in item:
                print_delay("\nAs the " + option + " moves to attack, "
                            "you unsheath your new sword.")
                print_delay("\nThe Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_delay("\nBut the " + option + "takes one look at "
                            "your shiny new toy and runs away!")
                print_delay("\nYou have rid the town of the " + option +
                            ". You are victorious!\n")
            else:
                print_delay("\nYou do your best...")
                print_delay("but your dagger is no match for the "
                            + option + ".")
                print_delay("\nYou have been defeated!\n")
            restart_game()
            break
        if choice == "2":
            print_delay("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            cave_or_house(item, option)
            break


def cave_or_house(item, option):
    print_delay("Enter 1 to knock on the door of the house.")
    print_delay("Enter 2 to peer into the cave.")
    print_delay("What would you like to do?")
    while True:
        user_input = input("(Please enter 1 or 2.)\n")
        if user_input == "1":
            house(item, option)
            break
        elif user_input == "2":
            cave(item, option)
            break


def restart_game():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_delay("\n\n\nExcellent! Restarting the game ...\n\n\n")
        start_game()
    elif again == "n":
        print_delay("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        restart_game()


def start_game():
    item = []
    option = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                            "gorgon"])
    welcome_text(item, option)
    cave_or_house(item, option)


start_game()
