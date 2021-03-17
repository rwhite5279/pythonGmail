# pythonGmail
A Python script that sends email using your Gmail account

This basic Python3 script allow you to send email to someone from 
your Gmail account.

This script requires that you log in to your Google account and
enable unsafe operations (like letting a script have access to your
email account). From Google account:

    My Account > Sign-in & security > Allow less secure apps: ON

If you get an error message from Google similar to the following:

    smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and 
    Password not accepted. Learn more at\n5.7.8  
    https://support.google.com/mail/?p=BadCredentials b17sm17464411pfp.136 - gsmtp')

...it is possibly due to you not having approved "Less secure app access."

Note also that this script requires that the password for your
email account be placed in plaintext in this file. This is *very*
unsafe. There are ways to manage password security for a script,
but they aren't addressed in this basic script.

For safety, do not use an important Gmail account for this script.
An out-of-control script might cause you to run afoul of Google's
Gmail policies.

This most recent version of the script takes advantage of Python3's
`email` package. See the documentation for that package for assistance
in emailing multipart MIME messages, if needed.


@author Richard White, rwhite@crashwhite.com
@version 2021-03-16
