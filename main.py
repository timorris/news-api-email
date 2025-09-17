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
        <div style="display:flex flex-direction:row;padding:5px;justify-content:center;align-items:center;">
          <div style="width:100px;height:auto;border-radius:4px;overflow:hidden;margin-right:5px;display:flex:1">
            {'<a href=' + article["url"] + ' style="color:#666;text-decoration:none;hover:underline;"><img src=' + article["urlToImage"] + ' alt=' + article["title"] + ' style="width:100px;height:auto;border border-radius:4px;" /></a>' if article['urlToImage'] is not None and not article["urlToImage"].endswith('.webp') else ''}
          </div>
          <div style="display:flex:1">
            <div>
                <span style="color:#666;font-size:12px;"><em>Source: {article['source']['name']}: </em></span>
            </div>
            <a href='{article["url"]}' style="color:#666;text-decoration:none;hover:underline;">
             <b>{article['title']}</b>
            </a><br/>
            {article['description'] + "<br/>" if article['description'] is not None else ''}
          </div>
          <hr/>
        </div>
    """

send_email(body)
