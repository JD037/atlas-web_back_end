#!/usr/bin/env python3
""" Initialize Flask app """

from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all other view files after initializing app_views to avoid circular imports
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *

# Ensure User is loaded from the storage
User.load_from_file()
