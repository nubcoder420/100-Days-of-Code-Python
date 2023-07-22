

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


quarters = 0.25
dimes = 0.1
nickles = 0.05
pennies = 0.01


water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


def espresso():
    espresso_water = MENU['espresso']['ingredients']['water']
    espresso_coffee = MENU['espresso']['ingredients']['coffee']
    espresso_cost = MENU['espresso']['cost']
    return espresso_water, espresso_coffee, espresso_cost

def latte():
    latte_water = MENU['latte']['ingredients']['water']
    latte_milk = MENU['latte']['ingredients']['milk']
    latte_coffee = MENU['latte']['ingredients']['coffee']
    latte_cost = (MENU['latte']['cost'])
    return latte_water, latte_milk, latte_coffee, latte_cost


def cappuccino():
    cappuccino_water = MENU['cappuccino']['ingredients']['water']
    cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
    cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
    cappuccino_cost = (MENU['cappuccino']['cost'])
    return cappuccino_water, cappuccino_milk, cappuccino_coffee, cappuccino_cost

espresso_water, espresso_coffee, espresso_cost = espresso()
latte_water, latte_milk, latte_coffee, latte_cost = latte()
cappuccino_water, cappuccino_milk, cappuccino_coffee, cappuccino_cost = cappuccino()

def input_money():
    input_quarters = float(input('Enter how many quarters: '))
    input_dimes = float(input('Enter how many dimes: '))
    input_nickles = float(input('Enter how many nickles: '))

# ordered_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()














