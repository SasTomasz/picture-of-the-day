import json

import schedule
import streamlit as st

import api_helper
import app_logger


def job():
    api_helper.get_data_from_api()


if __name__ == "__main__":

    is_first_run = True

    if is_first_run:
        app_logger.set_new_logger('main')
        api_helper.get_data_from_api()
        is_first_run = False

    schedule.every().day.at('07:00').do(job)

    with open("./static/apod_info.json") as file:
        apod_info = json.loads(file.read())

    st.header(apod_info["title"], divider='rainbow')

    # Set video or image
    if not apod_info["media_type"] == "video":
        st.image("./static/apod.jpg")
    else:
        st.video(apod_info["video_url"])

    st.write(apod_info["explanation"])
    st.write("All above data comes from NASA API for Astronomy Picture of the Day")
    # st.write("You can get more knowledge about it on ")
    st.page_link("https://api.nasa.gov/", label="https://api.nasa.gov/")

    schedule.run_pending()


