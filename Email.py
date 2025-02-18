import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from datetime import datetime, timedelta

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
    #recipient_email = "infonam@fnbnamibia.com.na"
    cc_emails = [
        "rarnat@yahoo.com",
        "romarioarnat15@gmail.com",
        #carenamibia@fnbnamibia.com.na,
        #FraudEarlyDetection@fnb.co.za
    ]
    subject = "RE: 3D Authorization failed - [External Email] [REF:20241212_145804532]"
    
    # Create a more detailed email body
    body = f"""
Hi  There,

This is an automated notification regarding my unresolved 3D Authorization failure incident.
To ensure this matter receives the necessary attention, I have set up an automatic follow-up every six hours until the issue is resolved.

Transaction Details:
- Reference INC8277801
- Status: Failed

Additional Information:
- Error Type: 3D Authorization Error
- Impact: Transaction could not be completed
- Priority: High


If you need any further information or clarification, please don't hesitate to contact me.

Best regards,
Romario
"""

    while True:
        current_time = datetime.now()
        # Check if it's weekend (5 = Saturday, 6 = Sunday)
        if current_time.weekday() not in [5, 6]:
            send_email(sender_email, sender_password, recipient_email, cc_emails, subject, body)
            print(f"Next email will be sent at {(current_time + timedelta(hours=6)).strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Skipping email send - it's weekend ({current_time.strftime('%A')})")
        
        time.sleep(6 * 3600)  # Sleep for 6 hours

if __name__ == "__main__":
    print("Starting email sender (Monday-Friday only). Press Ctrl+C to stop.")
    send_periodic_email()
