import os
import json
import requests
import logging

from dotenv import load_dotenv

load_dotenv("..\..\secrets\.env")
api_key = os.environ.get("API_KEY")

logging.basicConfig(filename= "..\\..\\logs\\news_api_data.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def save_news_data():
    if api_key:
        logging.info("API key loaded successfully")
    else:
        logging.error("API key not found, please check .env file")

    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_key}"

    response = requests.get(url)

    with open("..\..\data\\news_api_data.json", "w") as f:
        json.dump(response.json(), f, indent=4)
        logging.info("Data saved successfully")

if __name__ == "__main__":
    save_news_data()
