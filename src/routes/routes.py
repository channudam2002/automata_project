from src import app
from flask import render_template, redirect, url_for, request, session
from src.helper import helper

finiteAutomata = helper.FiniteAutomata()


@app.route('/')
def root_page():
    return render_template('base.html')


@app.route('/page2', methods=["GET", "POST"])
def page2():
    if request.method == 'POST':
        session['stateNum'] = int(request.form.get('state_num'))
        return render_template('page3.html', state_num = int(request.form.get('state_num')))
    return render_template('page2.html')

@app.route('/page3', methods=["GET", "POST"])
def page3():
    if request.method == "POST":
        state_arr = request.form.get('state_arr')
        state_arr = state_arr.split(",")
        session['stateArr'] = state_arr
        return render_template('page5.html', state_arr=state_arr)
    return render_template('page3.html')

@app.route('/page4', methods=['GET', 'POST'])
def page4():
    return render_template('page4.html')

@app.route('/page5', methods=['GET', 'POST'])
def page5():
    if request.method == "POST":
        alpha_arr = request.form.get('alpha_arr')
        alpha_arr = alpha_arr.split(",")
        session['alphaArr'] = alpha_arr
        return render_template('page6.html', alpha_arr=alpha_arr, state_arr=finiteAutomata.stateArr)
    return render_template('page5.html')

@app.route('/page6', methods=["GET", "POST"])
def page6():
    if request.method == "POST":
        start_state = request.form.get('start_state')
        start_state_arr = []
        start_state_arr.append(start_state)
        session['startStateArr'] = start_state_arr
        return render_template('page7.html')
    return render_template('page6.html')

@app.route('/page7', methods=["GET", "POST"])
def page7():
    if request.method == "POST":
        final_state_arr = request.form.get("final_state_arr")
        final_state_arr = final_state_arr.split(",")
        session['finalStateArr'] = final_state_arr
        return render_template('page8.html', state_arr=session['stateArr'], alpha_arr=session['alphaArr'])
    return render_template('page7.html')
@app.route('/page8', methods=['GET', 'POST'])
def page8():
    tranFunc_obj = {}
    if request.method == "POST":
        for state in session['stateArr']:
            tranFunc_obj[state] = {}
            for alpha in session['alphaArr']:
                key = state + "-" + alpha
                tranFunc_obj[state][alpha] = request.form.get(key)
        session["tranFunc_obj"] = tranFunc_obj
        return render_template('option.html')
    return render_template('page8.html', state_arr=session['stateArr'], alpha_arr=session['alphaArr'])
@app.route('/page9', methods=["GET", "POST"])
def page9():
    if request.method == "POST":
        string = request.form.get("string")
        finiteAutomata = helper.FiniteAutomata()
        finiteAutomata.stateArr = session["stateArr"]
        finiteAutomata.alphaArr = session['alphaArr']
        finiteAutomata.stateNum = session['stateNum']
        finiteAutomata.startStateArr = session['startStateArr']
        finiteAutomata.finalStateArr = session['finalStateArr']
        finiteAutomata.tranFuncObj = session['tranFunc_obj']
        # print(session["stateArr"], session['alphaArr'], session['stateNum'], session['startStateArr'], session['finalStateArr'], session['tranFunc_obj'])
        message = finiteAutomata.processString(string)
        return render_template('page9.html', message=message)
    return render_template('page9.html')
@app.route('/options')
def option_page():
    return render_template('option.html')

@app.route('/options/minimize')
def option_minimize_page():
    finiteAutomata = helper.FiniteAutomata()
    finiteAutomata.stateArr = session["stateArr"]
    finiteAutomata.alphaArr = session['alphaArr']
    finiteAutomata.stateNum = session['stateNum']
    finiteAutomata.startStateArr = session['startStateArr']
    finiteAutomata.finalStateArr = session['finalStateArr']
    finiteAutomata.tranFuncObj = session['tranFunc_obj']
    message = finiteAutomata.minFa()
    return render_template('option.html', message=message)



# New route

# @app.route('/automata')
# def automata_home_page():
#     return render_template('automata/base.html')
# @app.route('/automata/state_name', methods=['GET', 'POST'])
# def automata_state_name_page():
#     if request.method == 'POST':
#         state_arr = []
#         state_num = int(request.form.get('state_num'))
#         for num in range(0, state_num):
#             state_arr.append(request.form.get('stateName-'+str(num)))

#         finiteAutomata.stateNum = state_num #assign to class prop
#         finiteAutomata.stateArr = state_arr #assign tp class prop
#         print(finiteAutomata.stateArr)
#     return render_template('automata/state_name.html')