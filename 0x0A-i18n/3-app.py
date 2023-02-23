#!/usr/bin/env python3
""" Parametrize templates """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)
""" ... """


class Config(object):
    """ ... """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
""" ... """


@app.route('/')
def root():
    """ ... """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """ ... """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
