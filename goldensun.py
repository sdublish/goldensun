""" Golden Sun helper functions"""

from collections import namedtuple


class Djinn:
    def __init__(self, element, name, hp, pp, attack, defense, agility, luck):
        Stat = namedtuple("Stat", ["hp", "pp", "attack", "defense", "agility", "luck"])
        self.element = element
        self.stats = Stat(hp, pp, attack, defense, agility, luck)
        self.ability = None

    def add_ability(self, ability):
        self.ability = ability


class GSChar:
    def __init__(self, name, element, stats, spells=None):
        Stat = namedtuple("Stat", ["e_power", "e_resist", "f_power", "f_resist",
                          "win_power", "win_resist", "wa_power", "wa_resist"])
        self.name = name
        self.stats = Stat(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], stats[7])
        self.element = element
        self.base_spells = spells
        self.classes = {}

    def add_class(self, class_name, class_info):
        self.classes[class_name] = class_info


class Spell:
    def __init__(self, name, info, aoe, series):
        self.name = name
        self.info = info
        self.aoe = aoe
        self.series = series

    def is_in_series(self, series):
        return self.series == series


class CharClass:
    def __init__(self, name, stats, series):
        # issue: one class can have two different sets of valid djinn
        self.name = name
        self.stats = stats
        self.spells = {}
        self.e_djinn = set()
        self.f_djinn = set()
        self.wa_djinn = set()
        self.win_djinn = set()
        self.series = series

    def set_max_djinn(self, max_e, max_f, max_wa, max_win):
        self.e_djinn = set(max_e)
        self.f_djinn = set(max_f)
        self.wa_djinn = set(max_wa)
        self.win_djinn = set(max_win)

    def is_valid_djinn_combo(self, e_djinn, f_djinn, wa_djinn, win_djinn):
        if (e_djinn + f_djinn + wa_djinn + win_djinn) > 7:
            return False

        return (e_djinn in self.e_djinn and f_djinn in self.f_djinn and wa_djinn in self.wa_djinn and win_djinn in self.win_djinn)

    def is_in_series(self, series):
        return self.series == series


def create_djinn_dict(input_file):
    """ Returns a dictionary of djinn based off text file given"""
    d_dict = {}

    # consider: having it read a csv file vs. a text file

    for line in open(input_file):
        info = line.strip().replace("--", "0").split()
        name, hp, pp, att, dfns, agi, lck, typ = info
        d_dict[name] = Djinn(typ, name, hp, pp, att, dfns, agi, lck)

    return d_dict


def create_char_dict(input_file):
    """ Returns a dictionary of characters based off text file given"""
    characters = {}

    for line in open(input_file):
        info = line.strip().split("|")
        char = info[0]
        spells = info[6]
        if spells == "None":
            characters[char] = GSChar(char, info[1], (info[2].split(",") + info[3].split(",") + info[4].split(",") + info[5].split(",")))
        else:
            characters[char] = GSChar(char, info[1], (info[2].split(",") + info[3].split(",") + info[4].split(",") + info[5].split(",")), spells)

    return characters

##############CODE SAVED FOR POSSIBLE FURTHER USE ##############################
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
