from flask import Flask, render_template, request
from newsapi import NewsApiClient
import requests


app = Flask(__name__)
newsapi = NewsApiClient(api_key = "4f25baa11f644f33b5ea71ce1475df5e")

#renders the home page 
@app.route("/")
def homepage():
    return render_template('gen_layout.html')

@app.route("/", methods=['POST'])
def homepage_search():
    #get the input value in the search text box
    topic = request.form['text'].split(" ")
    mylist = search(topic)
    return render_template('gen_layout.html', context = mylist)

@app.route("/tech")
def techpage():
    mylist = search(["technology"])

    return render_template('gen_layout.html', context = mylist)

@app.route("/tech", methods=['POST'])
def techpage_search():
    topic = request.form['text'].split(" ")
    topic.append("technology")
    mylist = search(topic)
    return render_template('gen_layout.html', context = mylist)

@app.route("/entertainment")
def entertainmentpage():
    mylist = search(["entertainment"])
    return render_template('gen_layout.html', context = mylist)

@app.route("/entertainment", methods=['POST'])
def entertainment_search():
    topic = request.form['text'].split(" ")
    topic.append("entertainment")
    mylist = search(topic)
    return render_template('gen_layout.html', context = mylist)

@app.route("/sports")
def sportspage():
    mylist = search(["sports"])
    return render_template('gen_layout.html', context = mylist)

@app.route("/sports", methods=['POST'])
def sports_search():
    topic = request.form['text'].split(" ")
    topic.append("sports")
    mylist = search(topic)
    return render_template('gen_layout.html', context = mylist)

def search(input):
    search_url = ("https://newsapi.org/v2/everything?q=" + " OR ".join(input) + "&sortBy=popularity&apiKey=4f25baa11f644f33b5ea71ce1475df5e")

    response = requests.get(search_url).json()
        
    articles = response['articles']

    desc_odd=[]
    news_odd=[]
    img_odd = []
    url_odd = []

    desc_even=[]
    news_even=[]
    img_even=[]
    url_even=[]

    for i in range(len(articles)):
        mine = articles[i]

        if(i%2 == 1):
            news_odd.append(mine['title'])
            desc_odd.append(mine['description'])
            img_odd.append(mine['urlToImage'])
            url_odd.append(mine['url'])
        else:
            news_even.append(mine['title'])
            desc_even.append(mine['description'])
            img_even.append(mine['urlToImage'])
            url_even.append(mine['url'])

    
    mylist = zip(news_odd, desc_odd, img_odd, url_odd, news_even, desc_even, img_even, url_even)

    return mylist

if __name__== "__main__":
    app.run(debug=True)