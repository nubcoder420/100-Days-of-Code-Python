import requests
import datetime as dt

#-------------- STEP 1 Create User Account ------------------#
USERNAME = "Your USERNAME here"
TOKEN = "Your TOKEN here"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_parameters)
# print(response.text)

#-------------- STEP 2 Create Graph Definition ------------------#

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Studying Graph",
    "unit": "hours",
    "type": "float",
    "color": "kuro",
}

header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=header)
# print(response.text)

#-------------- STEP 3 Graph ------------------#

# https://pixe.la/v1/users/nubcoder420/graphs/graph1.html

#-------------- STEP 4 Post Value to the Graph ------------------#

current_datetime = dt.datetime.now()
current_date = current_datetime.strftime("%Y%m%d")

post_value_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

post_parameters = {
    "date": current_date,
    "quantity": "6"
}

# response = requests.post(url=post_value_endpoint, json=post_parameters, headers=header)
# print(response.text)

#---------------- PUT Request ------------------#

put_parameters = {
    "quantity": "4.5"
}

# response = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20230905", json=put_parameters, headers=header)
# print(response.text)

#---------------- DELETE Request ------------------#

# response = requests.put(url=f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/20230905", headers=header)
# print(response.text)



