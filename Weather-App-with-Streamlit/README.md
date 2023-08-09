# Weather Data Web Scraping and Display

This is a small Python project that utilizes the Beautiful Soup library for web scraping and Streamlit for front-end display. The project fetches weather data from Google based on user input and presents it in a user-friendly format.

## Features

- Web scraping with Beautiful Soup to retrieve weather data from Google.
- User-friendly interface using Streamlit for displaying weather information.
- Dynamic display based on user input, providing real-time weather updates.

## Requirements

- Python (3.x recommended)
- Beautiful Soup
- Streamlit
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Saadat-Khalid/My-Data-Science-Projects.git
   cd My-Data-Science-Projects/Weather-App-with-Streamlit
   ```

2. Install the required packages using pip:
   ```bash
   pip install beautifulsoup4 streamlit requests
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run weather.py
   ```

2. Access the app via your web browser at `http://localhost:8501`.

3. Input the desired location for weather information and see the results displayed.

## Project Structure

```
your-weather-project/
│
├── weather_app.py          # Streamlit app code Web scraping logic using BS
├── README.md               # Project documentation (you are here)
└── requirements.txt        # List of required packages
```

## Acknowledgments

- Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/
- Streamlit: https://streamlit.io/
- Google (for providing weather information)

## License

This project is licensed under the [MIT License](LICENSE).

---
