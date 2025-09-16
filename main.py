import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-08-16&sortBy=publishedAt&apiKey={API_KEY}"

request = requests.get(url)
content = request.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])
