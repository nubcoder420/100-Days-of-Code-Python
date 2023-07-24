

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


QUARTERS = 0.25
DIMES = 0.1
NICKLES = 0.05
PENNIES = 0.01


def insert_coin():
    print('Please insert coins.')
    input_quarters = float(input('Enter how many quarters: '))
    input_dimes = float(input('Enter how many dimes: '))
    input_nickles = float(input('Enter how many nickles: '))
    input_pennies = float(input('Enter how many pennies: '))

    total_coins = round((input_quarters * QUARTERS) + (input_dimes * DIMES) + (input_nickles * NICKLES) + (
                input_pennies * PENNIES), 2)

    return total_coins

def order_complete(drink):
    print(f'Here is ${change} in change.')
    print(f'Here is your {ordered_drink}. Enjoy!')


total_income = 0

remaining_water = 0
remaining_milk = 0
remaining_coffee = 0

have_resources = True

while have_resources:

    ordered_drink = input('What would you like? (espresso/latte/cappuccino):\n').lower()

    if ordered_drink == 'off':
        exit()

    elif ordered_drink == 'report':
        pass

    total_money = insert_coin()  # total amount of coins inserted
    change = total_money - MENU[ordered_drink]['cost']  # change if there is any

    if ordered_drink == 'cappuccino':
        order_complete(ordered_drink)
        total_income += MENU['cappuccino']['cost']
        remaining_water = resources['water'] - MENU['cappuccino']['ingredients']['water']
        resources['water'] = remaining_water
        remaining_coffee = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
        resources['coffee'] = remaining_coffee
        remaining_milk = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
        resources['milk'] = remaining_milk

    elif ordered_drink == 'latte':
        order_complete(ordered_drink)
        total_income += MENU['latte']['cost']
        remaining_water = resources['water'] - MENU['latte']['ingredients']['water']
        resources['water'] = remaining_water
        remaining_coffee = resources['coffee'] - MENU['latte']['ingredients']['coffee']
        resources['coffee'] = remaining_coffee
        remaining_milk = resources['milk'] - MENU['latte']['ingredients']['milk']
        resources['milk'] = remaining_milk

    elif ordered_drink == 'espresso':
        order_complete(ordered_drink)
        total_income += MENU['espresso']['cost']
        remaining_water = resources['water'] - MENU['espresso']['ingredients']['water']
        resources['water'] = remaining_water
        remaining_coffee = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
        resources['coffee'] = remaining_coffee


    print(total_income)
    print(remaining_water)
    print(remaining_coffee)

