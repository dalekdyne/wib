import os


class MailOptions:
    def __init__(self):
        self.config = {
            "MAIL_TEMPLATES": "static/templates",
            "MAIL_SUBJECTS": "static/subjects",
        }

    def get_template(self, type):
        """
        Get the template mail for the given type
        :param type: Type of the mail
        :return: Template mail
        """
        return open(
            os.path.join(self.config["MAIL_TEMPLATES"], type + ".html"), "r"
        ).read()

    def get_subject(self, type):
        """
        Get the subject for the given type
        :param type: Type of the mail
        :return: Subject
        """
        return open(
            os.path.join(self.config["MAIL_SUBJECTS"], type + ".txt"), "r"
        ).read()
