from src import app
from flask import render_template, redirect, url_for

@app.route('/')
def root_page():
    return render_template('base.html')