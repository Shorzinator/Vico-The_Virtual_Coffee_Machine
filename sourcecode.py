from turtle import *
from shapes import *
from menu import *

creating_turtle()

marco.penup()
marco.goto(0, 0)
marco.color("black")
marco.write("Welcome to the 'Testudines coffee'. My name is Vico and I'll be your Virtual Coffee maker for the day. I hope you day has been pleasent so far? (Yes/No)")

def response():
	response_list = input().split()
    if any(response_list) == 'Yes' or any(response_list) == 'yes' or any(response_list) == 'yeah' or any(response_list) == 'Yeah':
        print("So good to hear that!")
    else:
        print("I hope my coffee will make you feel better")


print("\n")
print("So, what can I make for you today, you can choose from the menu below.")
print("\n")

printing_menu()

def deciding_coffee():
	switcher = {
		1: "Goth Latte",
		2: "Indeh Latte",
		3: "A Sweet little rain",
		4: "Ethiopia, Yirgacheffe",
		5: "Kenya",
		6: "Colombia",
		7: "Indinesia, Mandheling",
		8: "Guinnesepresso",
		9: "Gordan GF's Temptation",
		10: "Bailey's Misu Misu",
		11: "Tea",
		12: "Caffe Latte",
		13: "Cappuccino",
		14: "Flat White",
	}
