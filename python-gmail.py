#!/usr/bin/env python3
"""
python-gmail.py
This program uses Python to send email to someone from your Gmail
account.

This script requires that you log in to your Google account and
enable unsafe operations (like letting a script have access to your
email account). From Google account: 

    My Account > Sign-in & security > Allow less secure apps: ON

Note also that this script requires that the password for your 
email account be placed in a file called 'pw.txt', located in the
same directory as this file. This is marginally safer than placing 
the file in the script itself, but plaintext passwords are still
unsafe. There are ways to manage password security for a script, 
but they aren't addressed in this basic script.

For safety, do not use an important Gmail account for this script.
An out-of-control script might cause you to run afoul of Google's
Gmail policies.

"""

__author__ = "Richard White"
__version__ = "2021-03-16"

import smtplib
from email.message import EmailMessage

def mail(gmail_user, gmail_password, to, subject, text):
    """to is the recipient, subject is the subject line of the
    email, and text is the message that will be delivered in 
    the body of the email.
    """
    msg = EmailMessage()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(text)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    # next line establishes a connection with Google's smtp
    mailServer.ehlo()
    # use tls encryption
    mailServer.starttls()
    # identify to server again as encrypted connection
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_password)
    # mailServer.sendmail(gmail_user, to, msg)
    mailServer.send_message(msg)
    mailServer.quit()

def main():
    # Get the Gmail username from a separate file
    infile = open('gmail_username.txt')
    gmail_user = infile.read().rstrip()
    infile.close()
    # Password stored in separate file 
    infile = open('gmail_password.txt')
    gmail_password = infile.read().rstrip()
    infile.close()
    # This function call initiates the function defined above, 
    # with the parameters being the sender, intended recipient, the 
    # subject line, and the body of the message.
    recipient = "person@domain.com"  # replace with actual email
    subject = "This was sent by a script!"
    body = "Can you believe this was sent by a computer?\n\nIt was!\n\n"
    mail(gmail_user, gmail_password, recipient, subject, body)

if __name__ == "__main__":
    main()


