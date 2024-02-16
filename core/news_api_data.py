import os
import json
import requests
import logging
from dotenv import load_dotenv

load_dotenv(dotenv_path="..\\secrets\\.env", verbose=True)
<<<<<<< HEAD:core/py_code/news_api_data.py
api_key = os.getenv("API_KEY")
=======
api_key = os.getenv("news_api_API_KEY")
>>>>>>> 4107db33ac7efc671c1a9f4c46c18e0f439d194d:core/news_api_data.py

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

<<<<<<< HEAD:core/py_code/news_api_data.py
    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_key}"
=======
    url = f"https://newsapi.org/v2/top-headlines?language=en&apiKey={api_key}&page=4"
>>>>>>> 4107db33ac7efc671c1a9f4c46c18e0f439d194d:core/news_api_data.py

    response = requests.get(url)

    with open("..\\data\\news_api_data.json", "w") as f:
        json.dump(response.json(), f, indent=4)
        if response.status_code == 200:
            logging.info("Data saved successfully")

<<<<<<< HEAD:core/py_code/news_api_data.py
    return response.json()


if __name__ == "__main__":
    print(api_key)
    news_data()
=======
    return response.json()
>>>>>>> 4107db33ac7efc671c1a9f4c46c18e0f439d194d:core/news_api_data.py
