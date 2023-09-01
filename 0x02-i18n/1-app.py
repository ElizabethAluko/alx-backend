from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)

class Config(object):
    LANGUAGES = ["en", "fr"]


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('1-index.html')

if __name__ == '__main__':
    1-app.run()
