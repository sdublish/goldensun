"""Golden Sun app which can run in the console"""

import goldensun as gs

print("Welcome to the Golden Sun Info App!")
char_list = ["Isaac", "Garet", "Mia", "Ivan"]


user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit.")

while user_input.lower() != 'q':
    if user_input.lower() == 'c':
        char = input("What character are you interested in? ")

        while char not in char_list:
            print("This is not a Golden Sun character!")
            char = input("What character are you interested in? ")

        # TODO: build out functionality in this search

        user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit.")

    elif user_input.lower() == 'd':
        djinn_dict = gs.create_djinn_dict("djinn.txt")
        print("Would you like to search by djinn or element?")
        djinn_info = input("Type 1 to search by djinn or 2 to search by element.")

        while djinn_info not in "12":
            print("Please select a valid choice.")
            djinn_info = input("Type 1 to search by djinn or 2 to search by element.")

        if djinn_info == "1":
            user_djinn = input("What djinn do you want to learn about?")

            while user_djinn not in djinn_dict:
                print("This is not a valid djinn!")
                user_djinn = input("What djinn do you want to learn about?")

            for stat, value in djinn_dict[user_djinn].items():
                print("{} : {}".format(stat, value))

            user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit.")

        elif djinn_info == "2":
            user_elem = input("Type Earth, Fire, Wind, or Water.")

            while user_elem.lower() not in ["earth", "fire", "wind", "water"]:
                print("Please enter a valid input.")
                user_elem = input("Type Earth, Fire, Wind, or Water.")

            print([djinn for djinn in djinn_dict if djinn_dict[djinn]["Type"].lower() == user_elem])
            user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit.")

    elif user_input.lower != 'q':
        print("Please type in a valid command.")
        user_input = input("Type 'd' if you would like to look up djinn. Type 'c' if you would like to look up characters. Type 'q' to quit.")
