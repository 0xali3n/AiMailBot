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
    from_addresses = data.get('from_addresses')  # list of from emails
    recipients = data.get('recipients')  # comma-separated string or list
    subject = data.get('subject')
    message = data.get('message')

    if not all([from_addresses, recipients, subject, message]):
        return jsonify({'status': 'error', 'message': 'Missing from_addresses, recipients, subject, or message'}), 400

    # Normalize recipients to list
    if isinstance(recipients, str):
        to_list = [email.strip() for email in recipients.split(',') if email.strip()]
    else:
        to_list = [email.strip() for email in recipients if email.strip()]
    
    # Normalize from_addresses to list
    if isinstance(from_addresses, str):
        from_list = [email.strip() for email in from_addresses.split(',') if email.strip()]
    else:
        from_list = [email.strip() for email in from_addresses if email.strip()]

    if not to_list or not from_list:
        return jsonify({'status': 'error', 'message': 'No valid from or recipient emails provided.'}), 400

    # Distribute recipients among from addresses (no overlap)
    assignments = {from_addr: [] for from_addr in from_list}
    for idx, recipient in enumerate(to_list):
        from_addr = from_list[idx % len(from_list)]
        assignments[from_addr].append(recipient)

    results = []
    for from_addr, recipients_for_from in assignments.items():
        from_field = from_addr  # Already in 'Display Name <email>' format
        for recipient in recipients_for_from:
            print(f"Sending from: {from_field} to: {recipient}")
            response = requests.post(
                f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
                auth=("api", API_KEY),
                data={
                    "from": from_field,
                    "to": recipient,
                    "subject": subject,
                    "text": message
                }
            )
            print(f"Mailgun status: {response.status_code}")
            print(f"Mailgun response: {response.text}")
            if response.status_code == 200:
                results.append({"from": from_field, "recipient": recipient, "status": "success"})
            else:
                results.append({"from": from_field, "recipient": recipient, "status": "error", "message": response.text})

    all_success = all(r["status"] == "success" for r in results)
    return jsonify({
        "status": "success" if all_success else "partial",
        "results": results
    })

if __name__ == '__main__':
    app.run(debug=True) 