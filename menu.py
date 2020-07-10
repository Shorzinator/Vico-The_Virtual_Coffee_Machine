# This is a module for printing the menu
# The menu has been copied from a cafe's menu named 'Mellower Coffee'

import turtle
from shapes import *

def printing_menu():
	creating_turtle()

	draw_circle(marco, "green", 50, 25, 0)
	draw_circle(marco, "blue", 50, 0, 0)
	draw_circle(marco, "yellow", 50, -25, 0)

	marco.penup()
	marco.goto(0, -60)
	marco.color("black")
	marco.write("Pick your Poison: ", True, align = "right", font = "24pt bold")
	print("\n")
	marco.write("1. Goth Latte", True, align = "right", font = "16pt")
    marco.write("Consists of natural edible bamboo charcoal which benefits health by having a cleansing effect", True, align = "right", font = "10pt")

    print("\n")
	marco.write("2. Ondeh Latte", True, align = "right", font = "10pt")
    marco.write("Mellower dancing harmoniously with traditional ingredients of Southeast Asia", True, align = "right", font = "10pt")

	print("\n")
	marco.write("3. A Sweet Little Rain", True, align = "right", font = "10pt")
    marco.write("A cloud of sweetness raining on Mellower coffee", True, align = "right", font = "10pt")

	print("\n")
	marco.write("4. Ethiopia, Yirgacheffe", True, align = "right", font = "10pt")
    marco.write("Flora, Bergamot, Lemon", True, align = "right", font = "10pt")

	print("\n")
	marco.write("5. Kenya", True, align = "right", font = "10pt")
    marco.write("Tomato, Brown Sugar, Cranberry", True, align = "right", font = "10pt")

	print("\n")
	marco.write("6. Colombia", True, align = "right", font = "10pt")
    marco.write("Nutty, Green Grape", True, align = "right", font = "10pt")

	print("\n")
	marco.write("7. Indinesia, Mandheling", True, align = "right", font = "10pt")
    marco.write("Cocoa, Cream", True, align = "right", font = "10pt")

	print("\n")
	marco.write("8. GUINNESPRESSO", True, align = "right", font = "10pt")
    marco.write("Lemon juice, Espresso", True, align = "right", font = "10pt")

	print("\n")
	marco.write("9. GORDAN GF'S TEMPTATION", True, align = "right", font = "10pt")
    marco.write("Gordon gin, Ice drip, Yirgacheffe, Soda water", True, align = "right", font = "10pt")

	print("\n")
	marco.write("10. BAILEY'S MISU MISU", True, align = "right", font = "10pt")
    marco.write("Baileys, Milk, Cocoa powder", True, align = "right", font = "10pt")

	print("\n")
	marco.write("11. TEA", True, align = "right", font = "10pt")
    marco.write("English Breakfast, Osmanthus, Chamomile Dream, Lemon Ginger, Mint, Straits Chai, Earl Grey Lavender", True, align = "right", font = "10pt")

	print("\n")
	marco.write("12. CAFFE LATTE", True, align = "right", font = "10pt")
    marco.write("30ml espresso, 65-degree steamed milk, 0.5cm milk foam", True, align = "right", font = "10pt")

	print("\n")
	marco.write("13. CAPPUCCINO", True, align = "right", font = "10pt")
    marco.write("30ml espresso, 65-degree steamed milk, 1cm milk foam", True, align = "right", font = "10pt")

	print("\n")
	marco.write("14. FLAT WHITE", True, align = "right", font = "10pt")
    marco.write("30ml espresso, 65-degree steamed milk, 0.3cm milk foam", True, align = "right", font = "10pt")
