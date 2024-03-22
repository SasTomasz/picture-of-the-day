import json
import logging

import requests
import streamlit as st


def check_data_type(data: any):
    return data["media_type"]


def get_data_from_api():
    # Get data from apod
    api_key = st.secrets['API_KEY']
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    r = requests.get(url).json()

    try:
        video_url = r["url"]

        if not r["media_type"] == "video":
            # Get and save image
            image_url = r['hdurl']
            image = requests.get(image_url).content

            with open("./static/apod.jpg", "wb") as file:
                file.write(image)

            video_url = "Empty"

        # Construct json
        image_info = {"title": r["title"], "explanation": r["explanation"],
                      "media_type": r["media_type"], "video_url": video_url}
        json_object = json.dumps(image_info, indent=4)

        with open("./static/apod_info.json", "w") as file:
            file.write(json_object)

        return r
    except KeyError as error:
        logger.error(error)


if __name__ == "__main__":
    logger = logging.getLogger('temp')
    response = get_data_from_api()
    logger.info(response)
else:
    logger = logging.getLogger('main')
