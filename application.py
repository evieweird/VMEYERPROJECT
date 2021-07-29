from flask import Flask, render_template
from rdkit import Chem
from rdkit.Chem import Draw 
from rdkit.Chem.Draw import rdMolDraw2D
from flask import Markup

application = Flask(__name__, template_folder='template')

@application.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@application.route('/database/', methods=['GET', 'POST'])
def database():
    return render_template('database.html')
