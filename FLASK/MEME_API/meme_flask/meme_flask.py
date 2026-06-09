#!/bin/python

from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_meme():
    # uncomment these two lines and comment out the other url line if you want to use a specific subreddit
    # sr = "/wholesomememes"
    # url = "https://meme-api.com/gimme" + sr
    url = "https://meme-api.com/gimme"
    response = requests.get(url).json()
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)

app.run(host="0.0.0.0", port=80)
