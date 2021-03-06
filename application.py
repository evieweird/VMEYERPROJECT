from flask import Flask, render_template


application = Flask(__name__, template_folder='template')

@application.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@application.route('/database/', methods=['GET', 'POST'])
def database():
    return render_template('database.html')
