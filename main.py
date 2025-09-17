import os
import requests
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

topic = "tesla"

url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2025-09-16&" \
       "sortBy=publishedAt&" \
       f"apiKey={API_KEY}&" \
       "language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles'][:20]:
    if article['title'] is not None:
        body += rf"""
        <div style="display:flex; flex-direction:row;width:100%;margin-bottom:10px;border-bottom:1px solid #666;padding:10px 0;">
          <div style="flex: 1;">
            {'<a href="' + article["url"] + '"><img src="' + article["urlToImage"] + '" alt="' + article["title"] + '" style="width:150px;height:auto;border-radius:5px;" /></a>' if article['urlToImage'] is not None and not article["urlToImage"].endswith('.webp') else ''}
          </div>
          <div style="flex: 2;">
            <div>
                <span style="color:#666;font-size:12px;"><em>Source: {article['source']['name']}: </em></span>
            </div>
            <a href="{article['url']}" style="color:blue;text-decoration:none;&hover:text-decoration:underline;">
             <b>{article['title']}</b>
            </a>
            <div style="margin-top:5px;">
              {article['description'] if article['description'] is not None else ''}
            </div>
          </div>
        </div>
    """

send_email(body)
