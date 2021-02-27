from flask import Flask, redirect, url_for

from .answer import Answer

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    return redirect(url_for('will_they_win'))


@app.route('/will-they-win/', methods=['GET'])
def will_they_win():
    return {'answer': Answer.negative()}
