#!/usr/bin/env python3
"""Basic Babel Setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configures the desired languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get the local languages from sys or browser or client settings"""
    user_locale = request.args.get('locale')

    if user_locale in app.config['LANGUAGES']:
        return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders index page to the browser"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
