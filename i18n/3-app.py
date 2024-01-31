#!/usr/bin/env python3
""" Create a basic Flask App
    with a single '/' route and an index.html template
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
# Instantiate Babel object in module-level variable babel
babel = Babel(app)


class Config():
    """ Configure available languages in our app """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Use Config class as config for our app
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Return user preferred locale, if not available return best match """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Return index.html template """
    from flask_babel import gettext as _
    return render_template('/3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
