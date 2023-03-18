from flask import Flask
import os
import sys
import logging
from loguru import logger


def create_app():
    logger.info("creating app")
    app = Flask(__name__,
                # static_url_path='/static',
                # static_folder='./hatchery/server/static_files',
                instance_relative_config=True)
    app_blueprints(app)
    logger.info(app.static_folder)
    logger.info(app.static_url_path)

    return app


def app_blueprints(app):
    with app.app_context():
        from .views import main_bp
        app.register_blueprint(main_bp, url_prefix='/')
