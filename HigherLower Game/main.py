from art import logo, vs
from game_data import data
import random


# data2 is for testing purposses
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


def generate_item():
    value_of_key = data[random.randint(0, len(data) - 1)]
    # value_of_key = data2[random.randint(0, len(data2) - 1)] # for tesssting code
    name = value_of_key['name']
    follower_count = value_of_key['follower_count']
    description = value_of_key['description']
    country = value_of_key['country']

    return name, follower_count, description, country

name_a, follower_count_a, description_a, country_a = generate_item()
name_b, follower_count_b, description_b, country_b = generate_item()

print(f"Compare A: {name_a}, a {description_a}, from {country_a}")
print(f"{follower_count_a}")
print(f"Against B: {name_b}, a {description_b}, from {country_b}")
print(f"{follower_count_b}")



# TODO: Access the follower_count and save it in a variable - DONE
# TODO: Compare user input
