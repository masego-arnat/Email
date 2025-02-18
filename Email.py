import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime

def send_email(sender_email, sender_password, recipient_emails, cc_emails, subject, body):
    """
    Send an email using Gmail SMTP server with CC functionality
    
    Args:
        sender_email (str): Your Gmail address
        sender_password (str): Your Gmail app password
        recipient_emails (str): Primary recipient's email address
        cc_emails (list): List of CC recipient email addresses
        subject (str): Email subject
        body (str): Email body content
    """
    # Create message container
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_emails
    message['Cc'] = ', '.join(cc_emails)
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        
        # Login to the server
        server.login(sender_email, sender_password)
        
        # Send email to all recipients (including CC)
        all_recipients = [recipient_emails] + cc_emails
        text = message.as_string()
        server.sendmail(sender_email, all_recipients, text)
        print(f"Email sent successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
        
    except Exception as e:
        print(f"Error sending email: {e}")
        
    finally:
        server.quit()

def send_periodic_email():
    # Email configuration
    sender_email = "romarioarnat15@gmail.com"
    sender_password = "jozt lwtx clwy egzp"
    recipient_email = "romarioarnat15@gmail.com"
    cc_emails = [
        "rarnat@yahoo.com",
        "romarioarnat15@gmail.com",
        "romarioarnat15@gmail.com"
    ]
    subject = "Periodic Test Email"
    body = "This is an automated email sent from Python every 6 hours!"

    while True:
        send_email(sender_email, sender_password, recipient_email, cc_emails, subject, body)
        time.sleep(6 * 3600)  # Sleep for 6 hours (6 * 3600 seconds)

if __name__ == "__main__":
    print("Starting email sender. Press Ctrl+C to stop.")
    send_periodic_email()
