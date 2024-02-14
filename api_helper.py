import requests
import streamlit as st

api_key = st.secrets['API_KEY']
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
response = requests.get(url)

with open("./assets/images/apod.jpg", "wb") as file:
    file.write(response.content)
