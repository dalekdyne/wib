from pydantic import BaseModel


class Mail(BaseModel):
    to: str
    type: str


class MailText(BaseModel):
    to: str
    subject: str
    body: str


class MailHtml(BaseModel):
    to: str
    subject: str
    body: str
