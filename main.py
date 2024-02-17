import schedule
import streamlit as st
import json

import api_helper


def job():
    api_helper.get_data_from_api()


schedule.every().day.at('07:00').do(job)

with open("./static/apod_info.json") as file:
    apod_info = json.loads(file.read())

st.header(apod_info["title"], divider='rainbow')
st.image("./static/apod.jpg")
st.write(apod_info["explanation"])

schedule.run_pending()
