#dictionary of coffee types, price, and resource requirments
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
#dictionary of available resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#this function will tell you cost of your coffee and ask for money from user then check if it is enough 
#if there is enough it will give back any change and remove required resources to make coffee from stock
def money(coffee_type):
    print("your", coffee_type, "is", MENU[coffee_type]["cost"])
    penny = .01
    nickel = .05
    dime = .1
    quarter = .25

    print("insert coins")

    quarter_change = float(input("how many quarters: ")) * quarter
    dime_change = float(input("how many dimes: ")) * dime
    nickel_change = float(input("how many nickel: ")) * nickel
    penny_change = float(input("how many pennies: ")) * penny
    total_change = quarter_change + dime_change + nickel_change + penny_change
    if MENU[coffee_type]["cost"] <= total_change:
        total_change -= MENU[coffee_type]["cost"]
        print(" here is your ", coffee_type)
        round_change = round(total_change, 2)
        print("here is your change: ", round_change)
        if coffee_type == "espresso":
            resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
        else:
            resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
            resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    elif MENU[coffee_type]["cost"] > total_change:
        print("you do not have enough money")
        print("here is your change back:", total_change)

# this function checks if stock has enough resources for requested coffee and tell you what resource is missing if not
def coffee_option(choices):
    if choices == "espresso":
        if MENU["espresso"]["ingredients"]["water"] < resources["water"] and MENU["espresso"]["ingredients"]["coffee"] < \
                resources["coffee"]:
            money(choices)
        elif MENU[choices]["ingredients"]["water"] > resources["water"]:
            print("not enough water")
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            print("not enough coffee")

    elif choices in MENU:
        if MENU[choices]["ingredients"]["water"] < resources["water"] and MENU[choices]["ingredients"]["coffee"] < \
                resources["coffee"] and MENU[choices]["ingredients"]["milk"] < resources["milk"]:
            money(choices)
        elif MENU[choices]["ingredients"]["water"] > resources["water"]:
            print("not enough water")
        elif MENU[choices]["ingredients"]["coffee"] > resources["coffee"]:
            print("not enough coffee")
        elif MENU[choices]["ingredients"]["milk"] > resources["milk"]:
            print("not enough milk")


power = "on"
#this offers options for checking resource levels, refilling resources, turning off machine, and choosing coffee type
while power != "off":
    choice = input("what would you like? espresso, cappuccino, or latte?: ")
    if choice == "off":
        power = "off"
    elif choice == "report":
        print(resources)
    elif choice == "refill":
        resources["milk"] = 200
        resources["water"] = 300
        resources["coffee"] = 100
    else:
        coffee_option(choice)
