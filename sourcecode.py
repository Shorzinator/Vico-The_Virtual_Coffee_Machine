from turtle import *
from shapes import *
from menu import *

creating_turtle()

marco.penup()
marco.goto(0, 0)
marco.color("black")
marco.write("Welcome to the 'Testudines Coffee'. My name is Vico and I'll be your Virtual Coffee Maker for the day. I hope your day has been pleasent so far? (Yes/No)")

def response():
	initial_response = input()
    if initial_response == 'Yes':
        print("So good to hear that!")
	elif initial_response == 'Hell, Yeah!':
		print("OMG! you sound like someone who just won a lottery! Would you be up for some recommendations to keep that energy up?")
		recomm_response = input()
	else:
        print("I hope my coffee will make you feel better")


print("\n")
print("So, what can I make for you today, you can choose from the menu below.")
print("\n")

printing_menu()

def recommendations():
	switcher_1 = {
		1: ""
	}


def deciding_coffee():
	switcher = {
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
	}
