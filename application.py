from flask import Flask, render_template
application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')