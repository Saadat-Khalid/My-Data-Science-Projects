import subprocess
import streamlit as st
import requests
from bs4 import BeautifulSoup

def install_packages():
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])

if __name__ == '__main__':
        install_packages()


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
    img = soup.find("img", class_="wob_tci")
    if img:
       img_url = "https:" + img["src"]  # Add the protocol (https://) to the image URL
       st.image(img_url)
    
    if location_info and temperature_info and time_info and weather_info:
        location = location_info.text
        temperature = temperature_info.text
        time = time_info.text
        weather = weather_info.text
        return location, temperature, time, weather
    else:
        return "Weather information not found."
            
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

loc = st.text_input("Enter Location:", value="Peshawar")

if st.button("Search"):
    col1, col2 = st.columns((2,1))
    
    loc, temp_f, time, weather = get_weather_data(loc)
    temp_c = fahrenheit_to_celsius(int(temp_f))  # Convert Fahrenheit to Celsius
    rounded_temp_c = round(temp_c)  # Round the temperature to the nearest integer
    
    with col1:
        st.title("Current Weather :earth_asia:")
        st.header(loc)
        st.header(f"{rounded_temp_c} °C")  # Display rounded temperature in Celsius
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

    
    
