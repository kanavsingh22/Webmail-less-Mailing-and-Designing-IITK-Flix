import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

smtp_port = 25                 
smtp_server = "mmtp.iitk.ac.in"

email_from = input('enter your email address:')
email_list = []

while True:
    add_email=input("Enter the email of recipient (or 'q' to quit):")
    if add_email=='q':
        break
    else:
        email_list.append(add_email)

pswd = input('enter your password:')

subject = input('enter the subject:')

body = input('enter your message:')

filename = input('enter filename:')

def send_emails(email_list):

    for individuals in email_list:

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = individuals
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, 'rb')
        
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        text = msg.as_string()

        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()

        print(f"Sending email to: {individuals}...")
        TIE_server.sendmail(email_from, individuals, text)
        print(f"Email sent to: {individuals}")
        print()

    TIE_server.quit()

send_emails(email_list)
