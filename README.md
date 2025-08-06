# Mailbot Flask Application

Mailbot is a simple, professional email campaign tool built with Flask and Mailgun. It features a modern web UI for sending personalized emails from multiple sender addresses to multiple recipients, with automatic distribution and per-recipient status tracking.

## Features

- **Welcome homepage**
- **Multi-sender support:** Select one or more professional sender addresses (e.g., `Name1 <cox1@imgnft.fun>`, `Name2 <cox2@imgnft.fun>`, etc.)
- **Multi-recipient support:** Add as many recipient email fields as you need
- **Automatic distribution:** Recipients are evenly distributed among selected senders (no overlap)
- **Live distribution preview:** See which sender will send to which recipients before sending
- **Per-recipient send results:** See which emails succeeded or failed
- **Uses Mailgun API:** API key and domain loaded from `.env`
- **Modern, clean frontend**

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
   MAILGUN_DOMAIN=imgnft.fun
   ```

   > **Note:** Only use sender addresses (the part after `<` in the UI) that are verified in your Mailgun account/domain.

4. **Run the application:**

   ```sh
   python app.py
   ```

5. **Open your browser and go to:**

   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Usage

- **Select sender addresses:**
  - Choose one or more from the list (e.g., `Name1 <cox1@imgnft.fun>`, `Name2 <cox2@imgnft.fun>`, ...)
  - Hold Ctrl (Windows) or Cmd (Mac) to select multiple
- **Add recipient emails:**
  - Use the "+" button to add as many recipient fields as needed
- **Fill in subject and message**
- **See the live distribution preview:**
  - The UI shows which sender will send to which recipients (no overlap)
- **Click "Send Email"**
- **View results:**
  - Each recipient receives their own email (not as CC/BCC)
  - The UI shows which emails succeeded or failed

## Example Sender Addresses

```
Name1 <cox1@imgnft.fun>
Name2 <cox2@imgnft.fun>
Name3 <cox3@imgnft.fun>
```

> **Tip:** You can customize the display names and addresses in `index.html` as long as the email part is verified in your Mailgun domain.

## Notes

- The Mailgun API key and domain are loaded from the `.env` file (never commit your real `.env` to GitHub).
- Only use sender addresses that are verified in your Mailgun account/domain to avoid deliverability issues or "via" warnings.
- This is a development server. For production, use a WSGI server like Gunicorn or uWSGI.

---

**Happy Emailing 😄!**
