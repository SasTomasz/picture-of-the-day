import requests
import streamlit as st


def get_data_from_api():
    # Get data from apod
    api_key = st.secrets['API_KEY']
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    r = requests.get(url).json()

    # Get image
    image_url = r['hdurl']
    image = requests.get(image_url).content

    with open("./static/apod.jpg", "wb") as file:
        file.write(image)

    with open("./static/apod.txt", "w") as file:
        file.write(r['explanation'])

    with open("./static/apod_title.txt", "w") as file:
        file.write(r['title'])
    return r


if __name__ == "__main__":
    response = get_data_from_api()
    print(response)
