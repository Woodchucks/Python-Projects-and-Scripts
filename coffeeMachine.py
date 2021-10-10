MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# from data import MENU
# from data import resources
# TODO 1. print start message/ ask for coffee choice
finalized = False
mashineMoney = 0
while not finalized:
    choice = input("What would you like? (esspresso/latte/cappuchino): ")
    # TODO 2. create report function, which prints the current status of water, milk, coffee, money
    def report():
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]} g')
        print(f"Money: ${mashineMoney}")
    # TODO 3. print report if asked
    if choice == "report":
        report()
    # TODO 4. create function which lowers ingredients after selling drink
    def lowerResources(drink):
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        if drink == "espresso":
            return
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    # TODO 5. if money inserted enough
    for drink in MENU:
        if drink == choice:
            drk = MENU[drink]["ingredients"]
            if drink == "espresso" and resources["water"] >= drk["water"] and resources["coffee"] \
            or resources["water"] >= drk["water"] and resources["coffee"] >= drk["coffee"] and resources["milk"] >= drk["milk"]:
                # TODO 6. print message to insert coins, ask how many quarters, dimes, nickles, pennies
                print("Please insert coins.")
                quarters = int(input("how many quarters?"))
                dimes = int(input("how many dimes?"))
                nickles = int(input("how many nickles?"))
                pennies = int(input("how many pennies?"))
                money = round(((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)), 2)
                if money >= MENU[drink]["cost"]:
                    # return change
                    change = round((money - MENU[drink]["cost"]),2)
                    print(f"Here is ${change} in change.")
                    #  print message about coffee bing ready
                    print(f"Here is your {choice}. Enjoy! :) ")
                    lowerResources(drink)
                    mashineMoney += MENU[drink]["cost"]
                else:
                    # print massage that transaction is not possible
                    # refund money
                    print(f"Sorry, that's not enough money. ${money} refunded.")
            else:
                print("Sorry, not enough ingredients to make coffee.")
