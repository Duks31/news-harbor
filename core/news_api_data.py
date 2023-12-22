import os
import json
import requests
import logging
from dotenv import load_dotenv

load_dotenv(dotenv_path="..\\secrets\\.env", verbose=True)
api_key = os.getenv("news_api_API_KEY")

logging.basicConfig(
    filename="..\\logs\\news_api_data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)

def news_data():
    if api_key:
        logging.info("API key loaded successfully")
    else:
        logging.error("API key not found, please check .env file")

    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_key}&page=4"

    response = requests.get(url)

    with open("..\\data\\news_api_data.json", "w") as f:
        json.dump(response.json(), f, indent=4)
        if response.status_code == 200:
            logging.info("Data saved successfully")

    return response.json()