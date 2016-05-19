# -*- coding: utf-8 -*-
from flask import Flask

from .views import bp


def create_app(config=None):
    app = Flask(__name__)
    app.config['WTF_CSRF_ENABLED'] = False

    app.register_blueprint(bp)

    return app
