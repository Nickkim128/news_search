from flask import Flask, render_template
from newsapi import NewsApiClient
import requests


app = Flask(__name__)

#renders the home page 
@app.route("/")
def homepage():

    return render_template('gen_layout.html')

@app.route("/tech")
def techpage():
    newsapi = NewsApiClient(api_key = "4f25baa11f644f33b5ea71ce1475df5e")

    tech_url = ("https://newsapi.org/v2/everything?q=technology&sortBy=popularity&apiKey=4f25baa11f644f33b5ea71ce1475df5e")

    response = requests.get(tech_url).json()
        
    articles = response['articles']

    desc=[]
    news=[]
    img = []

    for i in range(len(articles)):
        mine = articles[i]

        news.append(mine['title'])
        desc.append(mine['description'])
        img.append(mine['urlToImage'])

    mylist = zip(news, desc, img)


    return render_template('gen_layout.html', context = mylist)

@app.route("/entertainment")
def entertainmentpage():
    newsapi = NewsApiClient(api_key = "4f25baa11f644f33b5ea71ce1475df5e")
    enter_url= ("https://newsapi.org/v2/everything?q=entertainment&sortBy=popularity&apiKey=4f25baa11f644f33b5ea71ce1475df5e")

    response = requests.get(enter_url).json()
        
    articles = response['articles']

    desc=[]
    news=[]
    img = []

    for i in range(len(articles)):
        mine = articles[i]

        news.append(mine['title'])
        desc.append(mine['description'])
        img.append(mine['urlToImage'])

    mylist = zip(news, desc, img)


    return render_template('gen_layout.html', context = mylist)

@app.route("/sports")
def sportspage():
    newsapi = NewsApiClient(api_key = "4f25baa11f644f33b5ea71ce1475df5e")
    sport_url= ("https://newsapi.org/v2/everything?q=sports&sortBy=popularity&apiKey=4f25baa11f644f33b5ea71ce1475df5e")

    response = requests.get(sport_url).json()
        
    articles = response['articles']

    desc=[]
    news=[]
    img = []

    for i in range(len(articles)):
        mine = articles[i]

        news.append(mine['title'])
        desc.append(mine['description'])
        img.append(mine['urlToImage'])

    mylist = zip(news, desc, img)


    return render_template('gen_layout.html', context = mylist)

if __name__== "__main__":
    app.run(debug=True)