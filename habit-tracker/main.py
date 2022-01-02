import requests
from requests.api import head
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "liqingg"
TOKEN = "randomkeyformyselfwx"
GRAPH_ID = "test"

params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#step1 create a graph
#response = requests.post(url=pixela_endpoint, json=params)
#print(response.text)
#{"message":"Success. Let's visit https://pixe.la/@li , it is your profile page!","isSuccess":true}

graph_coinfig = {
    "id":GRAPH_ID,
    "name":"graph-name",
    "unit":"commit",
    "type":"int",
    "color":"sora"
}

#endpoint needs headers additionally
headers = {
    "X-USER-TOKEN": TOKEN
}
#step2 get a graph
#graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#response = requests.post(url=graph_endpoint, json=graph_coinfig, headers=headers)
#print(response.text)
#{"message":"Success.","isSuccess":true}

today = datetime(year=2021, month=12, day=31)
graph_value = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

#step3 post value to the graph
response = requests.post(url=value_endpoint, json=graph_value, headers=headers)
print(response.text)
#{"message":"Success.","isSuccess":true}

#setp4 modify the posted graph value 
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_value = {
    "quantity" : "4"
}
#response2 = requests.put(url=update_endpoint, json=new_pixel_value, headers=headers)
#print(response2.text)

#setp5 deleted the graph value 
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_endpoint, json=new_pixel_value, headers=headers)
#print(response.text)