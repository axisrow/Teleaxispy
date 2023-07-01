
import requests

class Teleaxispy:
    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"

    def get_updates(self, offset=None, timeout=30):
        params = {'timeout': timeout, 'offset': offset}
        response = requests.get(self.api_url + 'getUpdates', params)
        return response.json()['result']

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(self.api_url + 'sendMessage', params)
        return response

    def send_photo(self, chat_id, photo_url, caption=None):
        params = {'chat_id': chat_id, 'photo': photo_url, 'caption': caption}
        response = requests.post(self.api_url + 'sendPhoto', params)
        return response

    def send_document(self, chat_id, document_path, caption=None):
        with open(document_path, 'rb') as doc:
            params = {'chat_id': chat_id, 'caption': caption}
            response = requests.post(self.api_url + 'sendDocument', params, files={'document': doc})
        return response

    def get_groups(self):
        updates = self.get_updates()
        groups = []
        for update in updates:
            chat = update['message']['chat']
            if chat['type'] == 'group':
                groups.append(chat)
        return groups
