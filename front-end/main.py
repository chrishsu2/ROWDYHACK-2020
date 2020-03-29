# -*- coding: utf-8 -*-
# @Author: Christopher Hsu
# @Date:   2020-03-28 12:08:00
# @Last Modified by:   Christopher Hsu
# @Last Modified time: 2020-03-28 21:18:33

from flask import Flask, render_template, request, jsonify
#  import os

#import threading
import accessoryFunctions

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def splashpage():
    return render_template("splash.html")


urlTest="""http://ptsv2.com/t/9xfj1-1585431634/post"""

@app.route('/about', methods=["GET"])
def aboutpage():
    return render_template("aboutus.html")


@app.route('/results', methods=["POST"])
def searchresults():
    search_string = request.form["searchbar"]
    print(search_string)
    #postData2Svr(search_string,urlTest)
    #  TODO: second RESTful call to backend server
    #  TODO: send some placeholder blank images like all cool websites do nowadays
    #  and replace the blank images with javascript once the results/data from the call come back
    #  TODO: replace placeholder results page
    return render_template("searchresults.html", search_query=search_string)



if __name__ == "__main__":
    app.run()
