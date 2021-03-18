#!/usr/bin/env python3
"""
python-gmail.py
This program uses Python to send email to someone from your Gmail
account.

This script requires that you log in to your Google account and
enable unsafe operations (like letting a script have access to your
email account). From Google account: 

    My Account > Sign-in & security > Allow less secure apps: ON

Note also that this script requires that the username for your 
Gmail account be placed in a text file called `gmail_username.txt`,
and the password for that Gmail account be placed in a file called`gmail_password.txt`, with both of these files located in the
same directory as this file. This is marginally safer than placing 
that information in the script itself, but plaintext passwords are 
still unsafe. There are ways to manage password security for a script, 
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
    """gmail_user = the sender
       gmail_password = password for senders Gmail account
       to = the recipient's email
       subject = subject is the subject line of the email
       text = the message that will be delivered in email body
    """
    # Set up Python EmailMessage object as msg
    msg = EmailMessage()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(text)
    # Establish server object for connecting to email server at the
    # indicated port. This object has methods we can use to send emails.
    # Sweigart, in "Automate the Boring Stuff with Python" says that
    # a server may not support TLS on 587. In that case, use 
    # smtplib.SMTP_SSL() and port 465 instead.
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    # Establish a connection with Google's smtp server
    mailServer.ehlo()
    # Use tls encryption
    mailServer.starttls()
    # Log in to the server using credentials
    mailServer.login(gmail_user, gmail_password)
    # Send the email that we composed
    mailServer.send_message(msg)
    # Disconnect from the server
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


