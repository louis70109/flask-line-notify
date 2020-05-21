import uuid
from flask import Flask, render_template, request
import os

from lotify.client import Client

app = Flask(__name__)

CLIENT_ID = os.getenv('LINE_CLIENT_ID')
SECRET = os.getenv('LINE_CLIENT_SECRET')
URI = os.getenv('LINE_REDIRECT_URI')
lotify = Client(client_id=CLIENT_ID, client_secret=SECRET, redirect_uri=URI)


# or use by default
# lotify = Client()


@app.route('/')
def home():
    link = lotify.get_auth_link(state=uuid.uuid4())
    return render_template('notify_index.html', auth_url=link)


@app.route('/callback')
def confirm():
    token = lotify.get_access_token(code=request.args.get('code'))
    return render_template('notify_confirm.html', token=token)


@app.route('/notify/send', methods=['POST'])
def send():
    payload = request.get_json()
    response = lotify.send_message(
        access_token=payload.get('token'),
        message=payload.get('message')
    )
    return {'result': response.get('message')}, response.get('status')


@app.route('/notify/send/sticker', methods=['POST'])
def send_sticker():
    payload = request.get_json()
    response = lotify.send_message_with_sticker(
        access_token=payload.get('token'),
        message=payload.get('message'),
        sticker_id=630,
        sticker_package_id=4
    )
    return {'result': response.get('message')}, response.get('status')


@app.route('/notify/send/url', methods=['POST'])
def send_url():
    payload = request.get_json()
    response = lotify.send_message_with_image_url(
        access_token=payload.get('token'),
        message=payload.get('message'),
        image_fullsize=payload.get('url'),
        image_thumbnail=payload.get('url')
    )
    return {'result': response.get('message')}, response.get('status')


@app.route('/notify/send/path', methods=['POST'])
def send_file():
    payload = request.get_json()
    response = lotify.send_message_with_image_file(
        access_token=payload.get('token'),
        message=payload.get('message'),
        file=open('./test_data/dog.png', 'rb')
    )
    return {'result': response.get('message')}, response.get('status')


@app.route('/notify/revoke', methods=['POST'])
def revoke():
    payload = request.get_json()
    response = lotify.revoke(access_token=payload.get('token'))
    return {'result': response.get('message')}, response.get('status')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
