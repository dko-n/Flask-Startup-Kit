'''
    name: gmail.py
    description: Application file.
    author: On Kato
'''

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

class Gmail:
    def __init__(self, account, password):
        self.account = account
        self.password = password
        
    def send(self, subject="", body="", to="", type="plain"):
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(self.account, self.password)
        except OSError as e:
            raise Exception(e)
        except smtplib.SMTPAuthenticationError as e:
            raise Exception(e)
        except Exception as e:
            raise Exception(e)

        message = MIMEText(body, type)
        message['Subject'] = subject
        message['From'] = self.account
        message['To'] = to
        message['Date'] = formatdate()

        try:
            smtp.send_message(message)
        except Exception as e:
            raise Exception(e)
        finally:
            smtp.close()

# if __name__ == "__main__":
#     g = Gmail(account="", password="")
#     g.send("メール送信テスト", "<p>メール送信テスト</p>", "to", "html")