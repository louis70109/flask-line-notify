import requests
from flask import Flask, render_template, request
import os

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID')
SECRET = os.getenv('CLIENT_SECRET')
URI = os.getenv('REDIRECT_URI')


@app.route('/')
def home():
    return render_template('notify_index.html', CLIENT_ID=CLIENT_ID, URI=URI)


@app.route('/callback')
def confirm():
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
        payload = r.json()
        return render_template('notify_confirm.html', token=payload.get('access_token'))
    return {'message': 'Error'}, 400


@app.route('/send', methods=['POST'])
def send():
    payload = request.get_json()
    r = requests.post(
        "https://notify-api.line.me/api/notify",
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': payload.get('token')
        },
        data={'message': payload.get('message')}
    )
    return {'result': r.text()}, r.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
