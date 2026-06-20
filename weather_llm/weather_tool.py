import requests
import os
from dotenv import load_dotenv
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    logger.error("WEATHER_API_KEY not found in environment variables")


def get_weather(city):
    """
    Fetch real-time weather data from OpenWeatherMap API
    
    Args:
        city (str): City name to fetch weather for
        
    Returns:
        dict: Weather data or error message
    """
    
    if not API_KEY:
        return {"error": "API Key not configured. Please add WEATHER_API_KEY to .env file"}
    
    try:
        # Clean city name
        city_clean = city.strip()
        
        # OpenWeatherMap API endpoint
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"q={city_clean}&appid={API_KEY}&units=metric"
        )
        
        logger.info(f"Fetching weather for city: {city_clean}")
        
        # Make request with timeout
        response = requests.get(url, timeout=5)
        
        # Log response status
        logger.info(f"API Response Status: {response.status_code}")
        
        if response.status_code == 404:
            return {"error": f"City '{city_clean}' not found. Please try another city name."}
        
        if response.status_code == 401:
            return {"error": "Invalid API Key. Please check your WEATHER_API_KEY in .env"}
        
        if response.status_code != 200:
            return {"error": f"API Error: {response.status_code}. Please try again later."}
        
        data = response.json()
        
        # Log raw data for debugging
        logger.info(f"API Response: {data}")
        
        # Extract weather data with safety checks
        try:
            weather_data = {
                "city": data.get("name", city_clean),
                "country": data.get("sys", {}).get("country", ""),
                "temperature": round(data["main"]["temp"], 1),
                "feels_like": round(data["main"].get("feels_like", data["main"]["temp"]), 1),
                "humidity": data["main"]["humidity"],
                "pressure": data["main"].get("pressure", "N/A"),
                "condition": data["weather"][0]["description"].title(),
                "condition_main": data["weather"][0]["main"],
                "wind_speed": round(data["wind"]["speed"], 1),
                "wind_deg": data["wind"].get("degree", "N/A"),
                "clouds": data.get("clouds", {}).get("all", "N/A"),
                "visibility": data.get("visibility", "N/A"),
                "sunrise": data.get("sys", {}).get("sunrise", "N/A"),
                "sunset": data.get("sys", {}).get("sunset", "N/A")
            }
            
            logger.info(f"Weather data extracted successfully: {weather_data}")
            return weather_data
            
        except KeyError as e:
            logger.error(f"Error extracting weather data: {e}")
            return {"error": f"Error processing weather data. Missing field: {e}"}
    
    except requests.exceptions.Timeout:
        return {"error": "Request timeout. Please try again."}
    
    except requests.exceptions.ConnectionError:
        return {"error": "Connection error. Please check your internet connection."}
    
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"error": f"Unexpected error: {str(e)}"}