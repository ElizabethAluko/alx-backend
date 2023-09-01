#!/usr/bin/env python3
"""Basic Flask App"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the index page to the browser"""
    return render_template('0-index.html')


if __name__ == '__main__':
    0-app.run()
