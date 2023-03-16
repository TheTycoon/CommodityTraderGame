# Functions to help drive the game

def main_menu(city):
    print("=========")
    print("Main Menu")
    print("=========")
    print()
    print("1. Buy Resources")
    print("2. Sell Resources")
    print("3. New Day Menu")

    choice = 0
    while choice < 1 or choice > 3:
        choice = int(input("Enter the number for your choice: "))

        if choice == 1:
            buying_menu(city)
        elif choice == 2:
            selling_menu(city)
        elif choice == 3:
            new_day_menu(city)
        else:
            print("INVALID CHOICE! TRY AGAIN:")


def buying_menu(city):
    print("Buying Menu")
    city.print_inventory_sell()


def selling_menu(city):
    print("Selling Menu")
    city.print_inventory_buy()


def new_day_menu(city):
    print("New Day Menu")





