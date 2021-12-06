import requests
from pprint import pprint


class YaUploader:

    def __init__(self, token: str):
        self.token = token    

    def get_upload_link(self, path_to_file):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {'path': path_to_file, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, path_to_file):
        href = self.get_upload_link(path_to_file=path_to_file).get('href')
        filename = path_to_file.split('/')[-1]
        response = requests.put(href, data=open(filename, 'rb'))

if __name__ == '__main__':
    path_to_file = input()
    token = input()    
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)