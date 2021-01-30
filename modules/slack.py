
'''
    name: app.py
    description: Application file.
    author: On Kato
'''

import mimetypes
import requests

BASE_URL = "https://slack.com/api/chat.postMessage?"
TOKEN = "TOKEN"

class Slack:
    def __init__(self):
        pass

    def post_message(self, channel, message):
        try:
            url = BASE_URL
            token = "token={}".format(TOKEN)
            channel = "&channel={}".format(channel)
            message = "&text={}".format(message)
            result = requests.get(url + token + channel + message)
        except requests.exceptions.ConnectionError as e:
            raise Exception(e)
        except Exception as e:
            raise Exception(e)

        return result.status_code

if __name__ == "__main__":
    s = Slack()
    print(s.post_message("general", "送信テスト"))