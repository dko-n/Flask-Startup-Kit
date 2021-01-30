'''
    name: app.py
    description: Application file.
    author: On Kato
'''

import mimetypes
import requests

BASE_URL = 'https://api.chatwork.com/v2'
ROOM_ID = "ROOM_ID" # ROOM_ID
API_KEY = "API_KEY"
POST_MESSAGE_URL = '{}/rooms/{}/messages'.format(BASE_URL, ROOM_ID)
POST_FILE_URL = '{}/rooms/{}/files'.format(BASE_URL, ROOM_ID)

class Chatwork:
    def __init__(self):
        pass

    def post_message(self, message):
        headers = { 'X-ChatWorkToken': API_KEY}
        params = { 'body': message }
        try:
            result = requests.post(POST_MESSAGE_URL,
                        headers=headers,
                        params=params)
        except requests.exceptions.ConnectionError as e:
            raise Exception(e)
        except Exception as e:
            raise Exception(e)

        return result.status_code

    def post_file(self, message, file_dir, file_name):
        bin = open(file_dir, 'rb')
        file_content_type = mimetypes.guess_type(file_name)[0]
        headers = { 'X-ChatWorkToken': API_KEY}
        files = {
            'file': (file_name, bin, file_content_type),
            'message': message,
        }
        params = { 'body': message }
        try:
            result = requests.post(POST_FILE_URL,
                        headers=headers,
                        params=params,
                        files=files)
        except requests.exceptions.ConnectionError as e:
            raise Exception(e)
        except Exception as e:
            raise Exception(e)        
        
        return result.status_code

if __name__ == "__main__":
    c = Chatwork("Chatwork連携テスト(◜௰◝)")
    c.post()