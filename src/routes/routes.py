from src import app
from flask import render_template, redirect, url_for
from src.helper import helper


@app.route('/')
def root_page():
    return render_template('base.html')

@app.route('/options')
def option_page():
    return render_template('option.html')