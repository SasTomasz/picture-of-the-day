import requests
import streamlit as st

# Get data from apod
api_key = st.secrets['API_KEY']
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url).json()

# Get image
image_url = response['hdurl']
image = requests.get(image_url).content

with open("./assets/images/apod.jpg", "wb") as file:
    file.write(image)

with open("./assets/data/apod.txt", "w") as file:
    file.write(response['explanation'])

with open("./assets/data/apod_title.txt", "w") as file:
    file.write(response['title'])

print(response)
