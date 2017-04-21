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
email account be placed in plaintext in this file. This is *very*
unsafe. There are ways to manage password security for a script, 
but they aren't addressed in this basic script.

For safety, do not use an important Gmail account for this script.
An out-of-control script might cause you to run afoul of Google's
Gmail policies.

@author Richard White
@version 2017-04-20
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

# Change this to your Gmail account that you're sending FROM
gmail_user = "yourgmailaccount@gmail.com" 

# Password to authenticate use of Gmail account. Unsafe!
gmail_pwd = "yourpassword"      

def mail(to, subject, text):
    """to is the recipient, subject is the subject line of the
    email, and text is the message that will be delivered in 
    the body of the email.
    """
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    # next line establishes a connection with Google's smtp
    mailServer.ehlo()
    # use tls encryption
    mailServer.starttls()
    # identify to server again as encrypted connection
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    mailServer.quit()

# This function call initiates the function defined above, 
# with the parameters being the intended recipient, the 
# subject line, and the body of the message.
mail("recipient@someISP.com",
    "Your subject line goes here",
    "This is the body of the email.\n\nPut your text in here and it will be delivered via email.")
