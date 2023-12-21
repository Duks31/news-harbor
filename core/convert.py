import csv
import json
import logging

with open('..\\data\\news_api_data.json') as f:
    data = json.load(f)

articles_data = []

articles = data.get('articles', [])

for article in articles:
    source_name = article["source"]["name"]
    author = article["author"]
    title = article["title"]
    description = article["description"]
    content = article["content"]
    url = article["url"]

    articles_data.append([source_name, author, title, description, content, url])

with open('..\\data\\data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
    'Source Name', 'Author', 'Title', 'Description', 'Content', 'URL'   
    ])
    logging.info("Data CONVERTED successfully")
    writer.writerows(articles_data)