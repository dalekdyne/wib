import smtplib
from email.mime.text import MIMEText
import ssl


class MailClient:
    def __init__(self, username, password, host, port):
        self.username = username
        self.password = password
        self.smtp_server = host
        self.smtp_port = port
        context = ssl.create_default_context()
        self.smtp = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context)
        self.smtp.login(self.username, self.password)

    def check_connection(self):
        self.smtp.noop()

    def send_text_mail(self, to, subject, body):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = to
        self.smtp.sendmail(self.username, to, msg.as_string())

    def send_html_mail(self, to, subject, body):
        msg = MIMEText(body, "html")
        msg["Subject"] = subject
        msg["From"] = self.username
        msg["To"] = to
        self.smtp.sendmail(self.username, to, msg.as_string())
