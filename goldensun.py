# def check_djinn(n):
#     float_n = float(n).is_integer
#     if not float_n:
#         print("This is not an integer!")
#         return True

#     elif int(n) < 0:
#         print("Djinn number must be greater than zero!")
#         return True

#     elif int(n) > 7:
#         print("Djinn number must be seven or less!")
#         return True

#     return False


# e_djinn = input("How many Earth djinn are set? ")

# while check_djinn(e_djinn):
#     e_djinn = input("How many Earth djinn are set? ")

# f_djinn = input("How many Fire djinn are set? ")


# def get_djinn_number(djinn_type):
#     djinn_n = input("How many " + djinn_type + " djinn are set?")

#     while djinn_n is not None:
#         try:
#             djinn_n = int(djinn_n)
#         except TypeError:
#             print("This is not an integer!")
#             return None
#         if djinn_n > 7 or djinn_n < 0:
#             print("Valid djinn numbers are between 0 and 7. Please try again.")


def create_djinn_dict(input_file):
    """ Returns a dictionary of djinn based off text file given"""
    d_dict = {}

    for line in open(input_file):
        info = line.strip().replace("--", "0").split()
        name, hp, pp, att, dfns, agi, lck, typ = info
        d_dict[name] = {'HP': hp, 'PP': pp, "Attack": att, "Defense": dfns,
                        "Agility": agi, "Luck": lck, "Type": typ}

    return d_dict


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
        djinn_dict = create_djinn_dict("djinn.txt")
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
