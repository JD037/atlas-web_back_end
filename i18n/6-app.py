#!/usr/bin/env python3
"""Get Locale from Request - Sets up a Flask app
and configures Babel for internationalization."""
from flask import Flask, render_template, request, g, jsonify
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
    # First priority: Locale from URL parameters
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale

    # Second priority: Locale from user settings
    user_locale = getattr(g, 'user', {}).get('locale') if g.user else None
    if user_locale in app.config['LANGUAGES']:
        return user_locale

    # Third priority: Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])



users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Add a new function to retrieve a user
def get_user(user_id):
    if user_id:
        return users.get(int(user_id))
    return None

# Use the before_request decorator to run this function before other requests
@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    g.user = get_user(user_id)


@app.route('/')
def index():
    """Render the main page of the website.

    Returns:
        str: HTML content of the main page.
    """
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
