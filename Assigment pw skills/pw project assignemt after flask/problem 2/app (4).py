from flask import Flask , render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def get_news():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'apple',
        'from': '2024-01-30',
        'to': '2024-01-30',
        'sortBy': 'popularity',
        'apiKey': '70fc92e1861c42d1907b14d6abd60c6c'
    }
    response = requests.get(url, params=params)
    data = response.json()
    articles = data['articles']
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002)