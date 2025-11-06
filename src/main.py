import smtplib
import os
from dotenv import load_dotenv

# Load the .env file from the config folder
load_dotenv("auto-birthday-wisher/config/.env")

# Read environment variables
smtp_host = os.getenv("SMTP_HOST")
smtp_port = int(os.getenv("SMTP_PORT", "587"))
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_PASSWORD")

# recipients
recipients = [
    "otakora2025@gmail.com"
]

# the message
subject = "Hello Everyone!"
body = "Hi there! This is a test email sent to multiple people."
msg = f"Subject: {subject}\n\n{body}"


# create SMTP connection
with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.starttls()            # Secure the connection
    server.login(user=sender_email, password=sender_password)  # Authenticate
    server.sendmail(from_addr=sender_email, to_addrs=recipients, msg=msg)  # Send
    print("✅ Email sent securely!")
    
    
    