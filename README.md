# Mailbot Flask Application

This is a simple Flask application that displays a welcome message and allows you to send emails using Mailgun from the web interface.

## Features

- Welcome homepage
- Email sending form (recipient, subject, message)
- Uses Mailgun API (API key loaded from .env)

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

   Add your Mailgun API key:

   ```
   API_KEY=your-mailgun-api-key
   ```

4. **Run the application:**

   ```sh
   python app.py
   ```

5. **Open your browser and go to:**

   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

- Fill in the recipient email, subject, and message in the form.
- Click "Send Email".
- You will see a success or error message below the form.

## Notes

- The Mailgun API key is loaded from the `.env` file (never commit your real `.env` to GitHub).
- The sender is set as `Mailgun Sandbox <postmaster@imgnft.fun>` by default. You can change this in `app.py` if needed.
- This is a development server. For production, use a WSGI server like Gunicorn or uWSGI.

---

**Happy Emailing!**
