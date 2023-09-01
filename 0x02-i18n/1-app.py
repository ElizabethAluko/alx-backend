#!/usr/bin/env python3
"""Basic Babel Setup"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configures the desired languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """Renders index page to the browser"""
    return render_template('1-index.html')


if __name__ == '__main__':
    1-app.run()
