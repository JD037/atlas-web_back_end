#!/usr/bin/env python3
"""Get Locale from Request - Sets up a Flask app
and configures Babel for internationalization."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Configuration class for Babel.

    Attributes:
        LANGUAGES (list): a list of languages supported by the application.
        BABEL_DEFAULT_LOCALE (str): the default locale used by the application.
        BABEL_DEFAULT_TIMEZONE (str): the default timezone used
        by the application.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match language for the user's preferences.

    Returns:
        str: the best match language from the user's preferences.
    """
    user_locale = request.args.get('locale')
    if user_locale in app.config['LANGUAGES']:
        return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Render the main page of the website.

    Returns:
        str: HTML content of the main page.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
