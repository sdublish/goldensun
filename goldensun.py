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
