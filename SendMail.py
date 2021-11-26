def send_mail(user, app_pwd, recipient, subject, body, server, port):
    import smtplib
    from email.message import EmailMessage

    message = EmailMessage()
    message['From'] = user
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    with smtplib.SMTP(server, port, timeout = 15) as mail:
        mail.ehlo() # Identify ourselves
        mail.starttls() # Start encryption
        mail.ehlo() # Identify ourselves as encrypted
        mail.login(user, app_pwd)
        mail.send_message(message)
        mail.close()

send_mail(user = "test@gmail.com",
          app_pwd = "",
          recipient = "",
          subject = 'subject',
          body = 'body',
          server = "smtp.gmail.com",
          port = 587,)
