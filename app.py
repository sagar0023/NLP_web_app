from flask import Flask, render_template, request, redirect
from db import Database
import api

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name, email, password)

    if response:
        return render_template('login.html', message="Registration Successful. Kindly login to proceed")
    else:
        return render_template('register.html', message="Email already exists")

@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect email/password')

@app.route('/profile')
def profile():
    
    return render_template('profile.html')

@app.route('/ner')
def ner():
   
    return render_template('ner.html')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)
    return render_template('ner.html', response=response)


@app.route('/sentiment')
def sentiment():
   
    return render_template('sentiment.html')



@app.route('/do_sentiment', methods=['POST'])
def do_sentiment():
    text = request.form.get('sentiment_text')
    response = api.sentiment_analysis(text)
    sorted_sentiment = dict(sorted(response["sentiment"].items(), key=lambda item: item[1],reverse = True))

    
    return render_template('sentiment.html', response=sorted_sentiment)

@app.route('/emotion')
def emotion():
   
    return render_template('emotion.html')



@app.route('/perform_emotion', methods=['POST'])
def perform_emotion():
    text = request.form.get('emotion_text')
    response = api.emotion_prediction(text)
    sorted_emotion = dict(sorted(response["emotion"].items(), key=lambda item: item[1],reverse = True))

    
    return render_template('sentiment.html', response=sorted_emotion)
app.run(debug=True)
