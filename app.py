from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

@app.route('/')
def home():
    return render_template('index.html', message="Welcome to Mailbot!")

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    to = data.get('to')
    subject = data.get('subject')
    message = data.get('message')

    if not all([to, subject, message]):
        return jsonify({'status': 'error', 'message': 'Missing to, subject, or message'}), 400

    api_key = os.getenv('API_KEY', 'API_KEY')
    response = requests.post(
        "https://api.mailgun.net/v3/imgnft.fun/messages",
        auth=("api", api_key),
        data={
            "from": "Mailgun Sandbox <postmaster@imgnft.fun>",
            "to": to,
            "subject": subject,
            "text": message
        }
    )
    if response.status_code == 200:
        return jsonify({'status': 'success', 'message': 'Email sent successfully.'})
    else:
        return jsonify({'status': 'error', 'message': response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True) 