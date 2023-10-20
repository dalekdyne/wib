from config import Config
from core.smtp import MailClient


class ZohoMailClient(MailClient):
    def __init__(self):
        MailClient.__init__(
            self,
            username=Config.ZOHO_NO_REPLY_MAIL_ACCOUNT,
            password=Config.ZOHO_NO_REPLY_MAIL_ACCOUNT_PASSWORD,
            host=Config.ZOHO_MAIL_SERVER,
            port=Config.ZOHO_MAIL_PORT,
        )
