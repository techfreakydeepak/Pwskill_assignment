from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    youtube_data = scrape_youtube()
    amazon_data = scrape_amazon()
    return render_template('home.html', youtube_data=youtube_data, amazon_data=amazon_data)

def scrape_youtube():
    url = 'https://www.youtube.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Scrape the desired data from YouTube
    video_titles = [title.text for title in soup.select('#video-title')]
    return video_titles

def scrape_amazon():
    url = 'https://www.amazon.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Scrape the desired data from Amazon
    # For example, you can find product names using CSS selectors:
    product_names = [name.text for name in soup.select('.a-size-base-plus')]
    return product_names

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)