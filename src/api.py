from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def will_they_win():
    return {'answer': 'Not likely...'}
