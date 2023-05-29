import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(
        page_title="Weather App :cloud:",
        page_icon="🌍",
        # layout="wide",
    )

st.title("Weather App 🌧️ :sunny:")
st.markdown('''***Weather App by Saadat Khalid (Awan)***''')

def get_weather_data(location):
    url = f"https://www.google.com/search?q=weather+{location.replace(' ', '')}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    location_info = soup.find('span', class_='BBwThe')
    temperature_info = soup.find('span', class_='wob_t q8U8x')
    time_info = soup.find('div', class_='wob_dts')
    weather_info = soup.find("span", {"id": "wob_dc"})
    
    if location_info and temperature_info and time_info and weather_info:
        location = location_info.text
        temperature = temperature_info.text
        time = time_info.text
        weather = weather_info.text
        return location, temperature, time, weather
    else:
        return "Weather information not found."

loc = st.text_input("Enter Location:", value="Peshawar")

if st.button("Search"):
    col1, col2 = st.columns((2,1))
    
    loc, temp, time, weather = get_weather_data(loc)
    
    with col1:
        st.title("Current Weather :earth_asia:")
        st.header(loc)
        st.header(temp)
    with col2:
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.text(" ")
        st.subheader(time)
        st.text(" ")
        st.subheader(weather)

    
    