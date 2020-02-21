import requests
from flask import Flask, render_template, request, json, url_for
import os

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET = os.getenv('CLIENT_SECRET')
URI = os.getenv('REDIRECT_URI')

@app.route('/notify')
def home():
    return render_template('notify_index.html')


@app.route('/notify/check')
def check():
    client = {
        'grant_type': 'authorization_code',
        'code': request.args.get('code'),
        'redirect_uri': URI,
        'client_id': CLIENT_ID,
        'client_secret': SECRET
    }
    r = requests.post(
        'https://notify-bot.line.me/oauth/token', data=client)
    if r.status_code == 200:
        req = r.json()
        token = req['access_token']
        return render_template('notify_confirm.html', token=token)
    else:
        return {'message': 'Error'}, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
