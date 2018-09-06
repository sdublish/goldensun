"""Golden Sun app which can run in the console"""

import goldensun as gs

elements = set(["earth", "fire", "wind", "water"])
char_dict = gs.create_char_dict("characters.txt")
djinn_dict = gs.create_djinn_dict("djinn.txt")

print("Welcome to the Golden Sun Info App!")


user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit. ")

while user_input.lower() != 'q':
    if user_input.lower() == 'c':
        char = input("What character are you interested in? ")

        while char not in char_dict:
            print("This is not a Golden Sun character!")
            char = input("What character are you interested in? ")

        user_char = input("Would you like to know their preferred element or their stats? Type 'e' for element, 's' for stats.")

        while user_char.lower() not in "es":
            print("This is not a valid input!")
            user_char = input("Would you like to know their preferred element or their stats? Type 'e' for element, 's' for stats.")

        if user_char.lower() == "e":
            print("Preferred element: " + char_dict[char].element)

        elif user_char.lower() == "s":
            for stat, val in char_dict[char].stats._asdict().items():
                print("{} : {}".format(stat.replace("_", " "), val))

        user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit. ")

    elif user_input.lower() == 'd':
        print("Would you like to search by djinn or element?")
        djinn_info = input("Type 1 to search by djinn or 2 to search by element.")

        while djinn_info not in "12":
            print("Please select a valid choice.")
            djinn_info = input("Type 1 to search by djinn or 2 to search by element.")

        if djinn_info == "1":
            user_djinn = input("What djinn do you want to learn about? ")

            while user_djinn not in djinn_dict:
                print("This is not a valid djinn!")
                user_djinn = input("What djinn do you want to learn about? ")

            for stat, val in djinn_dict[user_djinn].stats._asdict().items():
                print("{}: {}".format(stat, val))

        elif djinn_info == "2":
            user_elem = input("Type Earth, Fire, Wind, or Water.")

            while user_elem.lower() not in elements:
                print("Please enter a valid input.")
                user_elem = input("Type Earth, Fire, Wind, or Water.")

            print([djinn for djinn in djinn_dict if djinn_dict[djinn].element.lower() == user_elem.lower()])

        user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit. ")

    elif user_input.lower != 'q':
        print("Please type in a valid command.")
        user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit. ")
