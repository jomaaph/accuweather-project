import os

import requests
from dotenv import load_dotenv

load_dotenv()
def connect_to_accuweather(country_code: str, location: str) -> dict:
    # Load environment variables
    URL = f"https://dataservice.accuweather.com/locations/v1/cities/{country_code}/search"

    API_KEY = os.getenv("API_KEY")    
    URL = os.getenv("URL")

    if not API_KEY:
        raise RuntimeError("API_KEY not configured in the environment or in the .env file")

    params = {"apikey": API_KEY, "q": location}
    # Make the request to the AccuWeather API
    try:
        headers ={
            "Authorization": "Bearer YOUR_API_KEY",
            "Accept-Encoding": "gzip",
        }
        response = requests.get(URL, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as error:
        print(f"Erro na requisicao: {error}")

    return data


connect_to_accuweather("Angola", "Luanda", "Luanda")


