import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Send an email using Gmail SMTP server
    
    Args:
        sender_email (str): Your Gmail address
        sender_password (str): Your Gmail app password
        recipient_email (str): Recipient's email address
        subject (str): Email subject
        body (str): Email body content
    """
    # Create message container
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable security
        
        # Login to the server
        server.login(sender_email, sender_password)
        
        # Send email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Error sending email: {e}")
        
    finally:
        server.quit()

# Example usage
if __name__ == "__main__":
    # Replace these with your actual details
    sender_email = "romarioarnat15@gmail.com"
    sender_password = "jozt lwtx clwy egzp"  # Use App Password, not your regular password
    recipient_email = "romarioarnat15@gmail.com"
    subject = "Test Email"
    body = "This is a test email sent from Python!"
    
    send_email(sender_email, sender_password, recipient_email, subject, body)
