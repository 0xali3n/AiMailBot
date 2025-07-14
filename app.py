from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN', 'MAILGUN_DOMAIN')
API_KEY = os.getenv('API_KEY', 'API_KEY')

@app.route('/')
def home():
    return render_template('index.html', message="Welcome to Mailbot!")

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    recipients = data.get('recipients')  # comma-separated string
    subject = data.get('subject')
    message = data.get('message')

    if not all([recipients, subject, message]):
        return jsonify({'status': 'error', 'message': 'Missing recipients, subject, or message'}), 400

    # Split and clean emails
    to_list = [email.strip() for email in recipients.split(',') if email.strip()]
    if not to_list:
        return jsonify({'status': 'error', 'message': 'No valid recipient emails provided.'}), 400

    results = []
    for recipient in to_list:
        print(f"Sending to: {recipient}")
        response = requests.post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", API_KEY),
            data={
                "from": f"Mailgun Sandbox <postmaster@{MAILGUN_DOMAIN}>",
                "to": recipient,
                "subject": subject,
                "text": message
            }
        )
        print(f"Mailgun status: {response.status_code}")
        print(f"Mailgun response: {response.text}")
        if response.status_code == 200:
            results.append({"recipient": recipient, "status": "success"})
        else:
            results.append({"recipient": recipient, "status": "error", "message": response.text})

    all_success = all(r["status"] == "success" for r in results)
    return jsonify({
        "status": "success" if all_success else "partial",
        "results": results
    })

if __name__ == '__main__':
    app.run(debug=True) 