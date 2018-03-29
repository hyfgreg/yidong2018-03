from config import Email
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def _format_msg(s):
    assert type(s) is str
    msg = MIMEText(s,'plain','utf-8')
    msg['Subject'] = Header('驿动api报错','utf-8').encode()
    return msg

def sendmail(s=None, to_addr=Email.to_addr):
    msg = _format_msg(s)
    server = smtplib.SMTP(Email.smtp_server, Email.smtp_port)
    server.set_debuglevel(1)
    server.starttls()
    server.login(Email.from_addr, Email.password)
    server.sendmail(Email.from_addr, [to_addr], msg.as_string())
    server.quit()
