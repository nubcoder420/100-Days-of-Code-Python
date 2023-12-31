
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


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

# result = {word: len(word) for word in sentence.split()}

# print(result)

#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
#
# weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
#
# print(weather_f)



import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_df = pandas.DataFrame(student_dict)
print(student_df)
