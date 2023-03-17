from src import app
from flask import render_template, redirect, url_for
from src.helper import helper


@app.route('/')
def root_page():
    return render_template('base.html')

@app.route('/page1')
def page_process():
    return render_template('process_string.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')



