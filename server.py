from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key = "TestKey"
counter = 0

def sessionCounter():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    sessionCounter()
    return render_template('index.html', counter=session['counter'])

@app.route('/plus2')
def plus2():
    session['counter'] += 1

    return redirect('/')

@app.route('/reset')
def reset():
    session['counter'] = 0
    return redirect('/')



app.run(debug=True)