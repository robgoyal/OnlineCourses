# Name: Application.py
# Author: Robin Goyal
# Last-Modified: May 28, 2017
# Purpose: Create Flask Application for displaying sentiment analysis
#          percentages of twitter user

from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer
import os
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))
    
    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, 100)

    # Check if tweets array contains None
    if tweets is None:
        sys.exit("Error: No tweets was returned!")
    
    # Absolute paths to lists 
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    # Initialize an Analyze object
    analyzer = Analyzer(positives, negatives)
    
    # Initialize sentiment analysis counts for chart values
    positive, negative, neutral = 0.0, 0.0, 0.0
    
    # Iterate through tweets 
    for tweet in tweets:
        
        # Return score analysis for tweet
        score = analyzer.analyze(tweet)
        
        # Increment respective sentiment analysis counts
        if score > 0.0:
            positive += 1
        elif score < 0.0:
            negative += 1
        else:
            neutral += 1
        
    # Set sentiment analysis counts to percentages
    positive = positive / 100
    negative = negative / 100
    neutral = neutral / 100

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
