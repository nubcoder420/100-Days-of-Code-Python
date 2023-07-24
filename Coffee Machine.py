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

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01

earnings = 0


def machine_off():
        exit()


def print_report():
    print('Current Resources:')
    for item, amount in resources.items():
        unit = 'ml' if item in ['water', 'milk'] else 'g'
        print(f"{item.capitalize()}: {amount}{unit}")

    print(f"Earnings: ${earnings:.2f}")


def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for item, amount in ingredients.items():
        if resources[item] < amount:
            print(f"Sorry, not enough {item} to make {drink}.")
            return False
        else:
            resources[item] -= amount
    return True



def input_coins(drink):
    print('Please insert coins.')

    try:
        user_quarters = int(input('How many quarters?: '))
        user_dimes = int(input('How many dimes?: '))
        user_nickels = int(input('How many nickles?: '))
        user_pennies = int(input('How many pennies?: '))

        total_input_coins = (user_quarters * QUARTERS) + (user_dimes * DIMES) + (user_nickels * NICKLES) + (user_pennies * PENNIES)

        change = total_input_coins - (MENU[drink]['cost'])

        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {drink}. Enjoy!")
    except ValueError:
        print('Invalid input.')


while True:

    ordered_drink = input('What would you like? (espresso/latte/cappuccino):\n').lower()

    if ordered_drink == 'off':
        machine_off()

    elif ordered_drink == 'report':
        print_report()

    elif ordered_drink == 'espresso' or ordered_drink == 'latte' or ordered_drink == 'cappuccino':
        if check_resources(ordered_drink):
            input_coins(ordered_drink)
            earnings += MENU[ordered_drink]['cost']

    else:
         print('Invalid input. Try again.')


# TODO: Refund the money if user inserted insufficient amount of coins
