
# LIST COMPREHENSION EXERCISES
#format
# new_list = [new_item for item in list if test]

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

# squared_numbers = [num ** 2 for num in numbers]
# result = [num for num in numbers if num % 2 == 0]

#Write your code 👆 above:

# print(squared_numbers)
# print(result)

# DICTIONARY COMPREHENSION
# format
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

result = {word: len(word) for word in sentence.split()}

print(result)



