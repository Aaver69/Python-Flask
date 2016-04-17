#! /usr/bin/python3
# -*- coding:utf-8 -*-

import logging

import sys

from flask import Flask
from flask_bootstrap import Bootstrap
import jinja2.ext
import webbrowser
from src.views import display_templates
from src.api import RestApi
from src.apios import Apios
from src.apibot import Apibot
logger = logging.getLogger(__name__)


def run_server():
    app = Flask(__name__, template_folder='src/templates')
    app.secret_key = 's3cr3t'
    api = RestApi("http://interface.onysos.fr")
    #   webbrowser.open("http://localhost:5000/config/list/")
    apios = Apios()
    apibot = Apibot(api, apios)
    Bootstrap(app)
    display_templates(app, api, apios, apibot)


def run_configs():
    pass


def main():
    if '-r' in sys.argv:
        run_configs()
    else:
        run_server()

if __name__ == "__main__":
    main()

