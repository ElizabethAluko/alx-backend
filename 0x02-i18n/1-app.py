#!/usr/bin/env python3
"""Basic Babel Setup"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configures the desired languages"""
    LANGUAGES = ["en", "fr"]


@babel.localeselector
def get_locale():
    """Get the local languages from sys or browser or client settings"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders index page to the browser"""
    return render_template('1-index.html')


if __name__ == '__main__':
    1-app.run()
