# Mailbot Flask Application

This is a simple Flask application that displays a welcome message and allows you to send emails using Mailgun from the web interface.

## Features

- Welcome homepage
- Email sending form with multiple recipient fields (add as many as you want)
- Each recipient receives their own individual email (no one sees other recipients)
- Uses Mailgun API (API key and domain loaded from .env)
- Shows per-recipient send results

## Setup Instructions

1. **Create a virtual environment (recommended):**

   On Windows:

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Create a `.env` file in the `Mailbot` directory:**

   Add your Mailgun API key and domain:

   ```
   API_KEY=your-mailgun-api-key
   MAILGUN_DOMAIN=yourdomain.com
   ```

4. **Run the application:**

   ```sh
   python app.py
   ```

5. **Open your browser and go to:**

   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

- Add as many recipient email fields as you need using the "+" button.
- Fill in the subject and message.
- Click "Send Email".
- Each recipient will receive their own email (not as CC/BCC).
- You will see a summary of which emails succeeded or failed below the form.

## Notes

- The Mailgun API key and domain are loaded from the `.env` file (never commit your real `.env` to GitHub).
- The sender is set as `Mailgun Sandbox <postmaster@yourdomain.com>` by default. You can change this in `app.py` if needed.
- This is a development server. For production, use a WSGI server like Gunicorn or uWSGI.

---

**Happy Emailing!**
