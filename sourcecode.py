import time
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed
import csv
import pandas as pd


full_menu = pd.read_csv(r'C:\Users\Shourya\Documents\My Projects\Virtual Coffee Maker\full_menu.csv')
recommended_menu = pd.read_csv(r'C:\Users\Shourya\Documents\My Projects\Virtual Coffee Maker\energetic_menu.csv')

for i in range(3):
    print(" 🎉", end="")
    time.sleep(0.7)

print("     Welcome to the 'TurCoffee'. My name is Vico and I'll be your Virtual Coffee Maker for the day. ")
print("I hope your day has been pleasant so far? (Hell, Yeah! / Yes / No)       ", end="")

print("🎉 🎉 🎉 ")

initial_response = input()

def response(initial_response = input()):
    """
	Input: Variable "initial_response" used to determine further course of action.
	Output: Two different types of menu's depending on the variable "initial_response".
    """
    if initial_response == 'Yes':
        print("So good to hear that!")
    elif initial_response == "Hell, Yeah!!":
        print("OMG! You sound like someone who just won a lottery! Would you be up for some recommendations to keep "
              "that energy up? Or should I just display the usual menu? (R: Recommendations, U: Usual Menu)")
        recommendation_response = input()
        if recommendation_response == "R":

            print("Printing Recommended Menu", end='')

            for i in range(5):
                print(".", end='')
                time.sleep(0.3)
            print(".")

            print(recommended_menu)

            print("\n")
            print("So, what can I make for you today, you can choose from the menu displayed.")
            print("\n")

        else:
            print("Printing Full Menu", end='')

            for i in range(5):
                print(".", end='')
                time.sleep(0.3)
            print(".")

            print(full_menu)

            print("\n")
            print("So, what can I make for you today, you can choose from the menu displayed.")
            print("\n")

    else:
        print("I hope my coffee will make you feel better")


def recommendations():
	"""
	Input: When 'recommendation_response = "R"', Recommendations() function is invoked.
	Output: Sources the recommended_menu() from the file menu.py
	"""

    print("Enter the number prefixed with your choice of coffee: ")
    choice_of_coffee = int(input())

    switcher_1 = {
        1: "Potence Affagato",
        2: "An Affair with Death",
        3: "Dope-Dope Doppio",
        4: "Bull Irish",
        5: "Evil Latte",
        6: "Macho Macchiato",
        7: "Complex Lungo",
        8: "Bull's Eye"  # Red Eye
    }


def deciding_coffee():
    switcher_2 = {
        1: "Goth Latte",
        2: "Indeh Latte",
        3: "A Sweet little rain",
        4: "Ethiopia, Yirgacheffe",
        5: "Kenya",
        6: "Colombia",
        7: "Indonesia, Mandheling",
        8: "Guinnesepresso",
        9: "Gordan GF's Temptation",
        10: "Bailey's Misu Misu",
        11: "Tea",
        12: "Caffe Latte",
        13: "Cappuccino",
        14: "Flat White",
        15: "Potence Affagato",
        16: "An Affair with Death",
        17: "Dope-Dope Doppio",
        18: "Bull Irish",
        19: "Evil Latte",
        20: "Macho Macchiato",
        21: "Complex Lungo",
        22: "Bull's Eye"
    }
