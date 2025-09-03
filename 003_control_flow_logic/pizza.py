print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
pizza_price = 0


if size.upper() == "S":
    pizza_price = 15
elif size.upper() == "M":
    pizza_price = 20
elif size.upper() == "L":
    pizza_price = 25
else:
    print("Wrong inputs.")

if pepperoni.upper() == "Y":
    if size.upper() == "S":
        pizza_price += 2
    else:
        pizza_price += 3

if extra_cheese.upper() == "Y":
    pizza_price += 1

print(f"Total Bill: ${pizza_price}")
