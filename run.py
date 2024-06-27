#!/usr/bin/env python3

"""Runs the spendwise application"""
import os
from dotenv import load_dotenv
from flask_session import Session
from flask import Flask, render_template, session
from spendwise.api.v1.auth import auth_bp
from spendwise.api.v1.expenses import app_views
from spendwise.api.v1.categories import app_views
from spendwise.api.v1.budgets import app_views
from spendwise.models import storage

app = Flask(
    __name__,
    template_folder='spendwise/templates',
    static_folder='spendwise/static',
)

# app-specific configurations
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the server-side session
Session(app)

# register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/v1')
app.register_blueprint(app_views, url_prefix='/api/v1')

