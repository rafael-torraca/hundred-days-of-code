from menu import MENU, resources


def report_machine():
    print()
    print(" Coffee Machine ".center(25, "-"))
    print(f"Water:  {resources["water"]}")
    print(f"Milk:   {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print("-" * 25)
    print()


def check_resources(resources, user_choice):
    r_water = resources["water"]
    r_coffee = resources["coffee"]
    r_milk = resources["milk"]
    water_menu = MENU[user_choice]["ingredients"]["water"]
    coffee_menu = MENU[user_choice]["ingredients"]["coffee"]
    if user_choice != "espresso":
        milk_menu = MENU[user_choice]["ingredients"]["milk"]
        if r_water >= water_menu and r_coffee >= coffee_menu and r_milk >= milk_menu:
            return
            
    


def check_user_choice():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "espresso":
        check_resources(resources, user_choice)
    elif user_choice == "latte":
        check_resources(resources, user_choice)
    elif user_choice == "cappuccino":
        check_resources(resources, user_choice)
    elif user_choice == "report":
        report_machine()
    elif user_choice == "off":
        pass
    else:
        print("Not valid!")
        check_user_choice()


check_user_choice()
money = 0


