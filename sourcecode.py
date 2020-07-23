import time
from turtle import *
from shapes import *
from menu import *


creating_turtle()

marco.penup()
marco.goto(0, 0)
marco.color("black")
marco.write("Welcome to the 'TurCoffee'. My name is Vico and I'll be your Virtual Coffee Maker for the day. I hope your day has been pleasent so far? (Hell, Yeah! / Yes / No)")

def response():
	initial_response = input()
    if initial_response == 'Yes':
        print("So good to hear that!")
	elif initial_response == 'Hell, Yeah!':
		print("OMG! You sound like someone who just won a lottery! Would you be up for some recommendations to keep that energy up? Or should I just display the usual menu? (R: Recommendations, U: Usual Menu)")
		recomm_response = input()
		if recomm_response == "R":
			print("\n")
			print("So, what can I make for you today, you can choose from the menu below.")
			print("\n")
			recommendations()
		else:
			print("\n")
			print("So, what can I make for you today, you can choose from the menu below.")
			print("\n")
			printing_main_menu()
	else:
        print("I hope my coffee will make you feel better")

def recommendations():
	print("Printing Recommended Menu", end = '')
	time.sleep(0.5)
	print(".", end = '')
	time.sleep(0.5)
	print(".", end = '')
	time.sleep(0.5)
	print(".", end = '')
	time.sleep(0.5)
	print(".", end = '')
	time.sleep(0.5)
	print(".", end = '')

	recommended_menu()

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
		8: "Bull's Eye"			# Red Eye
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
