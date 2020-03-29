# -*- coding: utf-8 -*-
# @Author: Christopher Hsu
# @Date:   2020-03-28 12:08:00
# @Last Modified by:   Christopher Hsu
# @Last Modified time: 2020-03-28 22:14:16

from flask import Flask, render_template, request, jsonify
from accessoryFunctions import getBackendResponse
#  import os

#import threading
import accessoryFunctions

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def splashpage():
    return render_template("splash.html")

@app.route('/about', methods=["GET"])
def aboutpage():
    return render_template("aboutus.html")

@app.route('/results', methods=["POST"])
def searchresults():
    search_string = request.form["searchbar"]
    backend_url = "https://back-end-dot-rowdyhacks-dev.appspot.com/api"
    #  hardcoded to https://www.walmart.com/store/1347/san-antonio-tx
    payload = {'query': search_string, 'grocerychain': "Walmart", 'store': "1347"}
    results = getBackendResponse(payload, backend_url).json()
    #postData2Svr(search_string,urlTest)
    #  TODO: second RESTful call to backend server
    #  TODO: send some placeholder blank images like all cool websites do nowadays
    #  and replace the blank images with javascript once the results/data from the call come back
    #  TODO: replace placeholder results page
    return render_template("searchresults.html", search_query=search_string, results=results)







if __name__ == "__main__":
    app.run()
