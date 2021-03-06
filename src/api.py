from flask import Flask, redirect, request, url_for

from src.answer import Answer

app = Flask(__name__)

TEAM_QUERY_PARAM = 'team'

@app.route('/', methods=['GET'])
def root():
    query_params_dict = {key: val for key, val in request.args.items() if key == TEAM_QUERY_PARAM}
    redirect_to_will_they_win_url = url_for('will_they_win', **query_params_dict)
    return redirect(redirect_to_will_they_win_url)


@app.route('/will-they-win/', methods=['GET'])
def will_they_win():
    team = request.args.get(TEAM_QUERY_PARAM)
    if not team:
        return {'status': 'error', 'error_message': 'missing team'}
    return {'status': 'ok', TEAM_QUERY_PARAM: team, 'answer': Answer.negative()}

