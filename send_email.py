import os
from dotenv import load_dotenv
import resend

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")

def send_email(message):
    html_content = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
      <div style="max-width: 600px; margin: 0 auto;padding: 20px;">
        <h2 style="color: #2563eb; border-bottom: 2px solid #e5e7eb; padding-bottom: 10px;">
            Your Latest News
        </h2>
        <div style="margin: 20px 0;">
          <div style="color:#666;background-color: #eee; padding: 15px; border-left: 4px solid #2563eb; border-radius: 4px;">
            {message}
          </div>
        </div>
      </div>
    </body>
    </html>
    """

    resend.api_key = RESEND_API_KEY

    params: resend.Emails.SendParams = {
        "from": "send@ohm.run",
        "to": ["timlmorris@pm.me"],
        "subject": "Today's News!",
        "html": html_content,
        "reply_to": "timorris@timorris.com"
    }

    email: resend.Emails.SendResponse = resend.Emails.send(params)
    print(email)


if __name__ == "__main__":
    send_email("Hello World!")
