from turtle import title
import requests
from ss import *

api_address = "https://newsapi.org/v2/everything?q=Apple&from=2022-10-07&sortBy=popularity&apiKey=" + key
json_data = requests.get(api_address).json()

ar = []

def news():
    for i in range(10):
        ar.append("Number " + str(i+1) + ": " + json_data["articles"][i]["title"] + ".")

    return ar

# arr = news()
# print(arr)
