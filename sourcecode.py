import turtle


print("Hi, my name is Vico and I'll be your Virtual Coffee maker for the day. I hope you day has been pleasent so far? (Yes/No)")
response = input()

if response == 'Yes' or response == 'yes':
	print("So good to hear that!")

else:
	print("I hope my coffee will make you feel better")

print("\n")

print("So, what can I make for you today, you caan choose from the menu below.")
print("\n")
print("Pick you poison: ".center(40, '-'))
printing_menu()
deciding_coffee()

def creating_turtle():
	marco = turtle.Turtle()
	marco.shape("turtle")
	marco.speed(5)


def printing_menu():
	print("1. Goth Latte")

def deciding_coffee():
