import sys
import smtplib
from email.message import EmailMessage
import os

# Check for required arguments
if len(sys.argv) < 5:
    print("Usage: python3 send_email.py <log_dir> <timestamp> <archive_file> <recipient_email>")
    exit(1)

# Get arguments
log_dir = sys.argv[1]
timestamp = sys.argv[2]
archive_file = sys.argv[3]
recipient_email = sys.argv[4]

# Get sender email and password from environment variables
sender_email = os.environ.get("EMAIL_SENDER")
email_pass = os.environ.get("EMAIL_PASS")
if not sender_email or not email_pass:
    print("Error: Set EMAIL_SENDER and EMAIL_PASS variables")
    exit(1)


msg = EmailMessage()
msg.set_content(f"Archive created for {log_dir} at {timestamp}: {archive_file}")
msg['Subject'] = "Log Archive Notification"
msg['From'] = sender_email
msg['To'] = recipient_email

# Attach the archive file
with open(archive_file, "rb") as f:
    file_data = f.read()
    file_name = os.path.basename(archive_file)
msg.add_attachment(file_data, maintype="application", subtype="gzip", filename=file_name)

# Send email via Gmail SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, email_pass)
        server.send_message(msg)
        print(f"Email sent to {recipient_email}")
except Exception as e:
    print(f"Error sending email: {e}")
    exit(1)
