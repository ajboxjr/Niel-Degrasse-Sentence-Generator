from flask import Flask, render_template
import sys
from markov import *


marky = Markov(read_file('neil.txt'),2)
app = Flask(__name__)

@app.route('/')
@app.route('/<int:number>')
def index(number=None):
    return render_template('home.html', sentence=marky.generate_sentence())
@app.route('/generate',methods=['POST'])
def generate():
    return marky.generate_sentence()

if __name__ == '__main__':
    app.run(debug=True)
