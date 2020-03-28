# -*- coding: utf-8 -*-
# @Author: Christopher Hsu
# @Date:   2020-03-28 12:08:00
# @Last Modified by:   Christopher Hsu
# @Last Modified time: 2020-03-28 12:39:21

from flask import Flask, render_template
#  import os


app = Flask(__name__)

@app.route('/')
def splashpage():
    return render_template("splash.html")

if __name__ == "__main__":
    app.run()
