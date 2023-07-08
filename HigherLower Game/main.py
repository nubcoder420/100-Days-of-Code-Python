from art import logo, vs
from game_data import data
import random



data2 = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
]

def first_item():
    value_of_key = data[random.randint(0, len(data) - 1)]
    name = value_of_key['name']
    follower_count = value_of_key['follower_count']
    description = value_of_key['description']
    country = value_of_key['country']

    return f"Compare A: {name}, a {description}, from {country}"

print(first_item())

def second_item():
    value_of_key = data[random.randint(0, len(data) - 1)]
    name = value_of_key['name']
    follower_count = value_of_key['follower_count']
    description = value_of_key['description']
    country = value_of_key['country']

    return f"Against B: {name}, a {description}, from {country}"

print(second_item())

result = first_item()
follower_count_variable = result.split(":")[1].split(" ")[2].strip()
print(follower_count_variable)