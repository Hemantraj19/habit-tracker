import requests
import datetime

USERNAME = "your_username"
TOKEN = "give_a_random_token"
GRAPHID = "any_name"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "studying",
    "unit": "hr",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"

current_date = str(datetime.date.today())
current_date = current_date.replace('-', '')
post_pixel_parameters = {
    "date": current_date,
    "quantity": input("How many hours did you study today?: "),
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
print(response.text)

update_pixel_endpoint = f"{post_pixel_endpoint}/{current_date}"
update_pixel_parameters = {
    "quantity": "8",
}

response = requests.put(url=update_pixel_endpoint, json=update_pixel_parameters, headers=headers)
print(response.text)

# delete_pixel_endpoint = update_pixel_endpoint
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
