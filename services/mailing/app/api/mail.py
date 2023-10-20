from fastapi import APIRouter, HTTPException

from app.mailing.service import MailService
from core.zoho_smtp import ZohoMailClient
from models.mails import Mail, MailText

router = APIRouter(tags=["mail"])

mail_client = ZohoMailClient()
mail_service = MailService(client=mail_client)


@router.post("/mail")
async def send_mail(mail: Mail):
    """
    Send a mail to the given recipient from static template
    :param to: Recipient
    :param type: Name of the mail template
    """
    try:
        mail_service.send_from_template(mail.to, mail.type)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/mail/text")
async def send_mail_text(mail: MailText):
    """
    Send a simple text mail to the given recipient
    :param to: Recipient
    :param subject: Subject of the mail
    :param body: Body of the mail
    """
    try:
        mail_service.send_from_text(mail.to, mail.subject, mail.body)
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
