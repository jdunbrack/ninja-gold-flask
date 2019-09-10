from flask import Flask, render_template, request, redirect, session, Markup
import random
import datetime

app = Flask(__name__)
app.secret_key = "ninja_gold"

@app.route('/', methods=["GET", "POST"])
def index():
    if 'reset' in request.form and request.form['reset'] == "True":
        session.clear()
        
    if not 'gold' in session:
        session['gold'] = 0
    if not 'log' in session:
        session['log'] = []
        session['log'].append(f"Game started! Time: {datetime.datetime.now()}")



    return render_template('index.html')


@app.route('/process_money', methods=["POST"])
def find_gold():
    area = request.form['area']
    rng = random.random()

    gold_gain = random.randint(int(request.form['min']), int(request.form['max']))
    session['gold'] += gold_gain

    if gold_gain < 0:
        session['log'].append("<span style='color: darkred;'>Spent some time gambling, and lost {} gold. Time: {}</span>".format(abs(gold_gain), datetime.datetime.now()))
    else:
        session['log'].append(f"Spent some time in the {area}, and earned {gold_gain} gold. Time: {datetime.datetime.now()}")    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
