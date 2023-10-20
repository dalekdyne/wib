from app.mailing.options import MailOptions


class MailService:
    def __init__(self, client):
        """
        :param client: Mail client
        """
        self.client = client
        self.options = MailOptions()

    def send_from_template(self, to, type):
        """
        Send a mail to the given recipient
        :param to: Recipient
        :param type: Type of the mail
        """
        message = self.options.get_template(type)
        subject = self.options.get_subject(type)
        self.client.send_html_mail(to, subject, message)

    def send_from_text(self, to, subject, body):
        """
        Send a mail to the given recipient
        :param to: Recipient
        :param subject: Subject of the mail
        :param body: Body of the mail
        """
        self.client.send_text_mail(to, subject, body)
