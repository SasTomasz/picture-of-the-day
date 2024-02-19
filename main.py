import schedule
import streamlit as st
import json

import api_helper

is_first_run = True

if is_first_run:
    api_helper.get_data_from_api()
    is_first_run = False


def job():
    api_helper.get_data_from_api()


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

schedule.run_pending()
