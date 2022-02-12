from bs4 import BeautifulSoup
from pip._vendor import requests

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/")
song = response.text
print('what year you would like to travel to in YYY-MM-DD format')
year = input()

soup = BeautifulSoup(response.text, "html.parser")
song_name_span = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_name_span]






