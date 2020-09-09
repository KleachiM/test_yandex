import requests
from pprint import pprint

class YaUploader:
    FILE_GET_URL = 'https://cloud-api.yandex.net:443/v1/disk/resources/files'
    FOLDER_INFO_URL = 'https://cloud-api.yandex.net:443/v1/disk/resources'

    def __init__(self, token: str):
        self.headers = {'Authorization': f'OAuth {token}'}
        self.params = {'path': 'disk:/'}

    def file_get(self):
        resp = requests.get(self.FILE_GET_URL, headers=self.headers)
        return resp.json()

    def folder_info(self, dir_name):
        resp = requests.get(self.FOLDER_INFO_URL, headers=self.headers, params = self.params)
        for dir in resp.json()['_embedded']['items']:
            if dir['type'] == 'dir' and dir['name'] == dir_name:
                return 'Folder found'

    def create_folder(self, dir_name):
        resp = requests.put(self.FOLDER_INFO_URL, headers=self.headers, params={'path':f'disk:/{dir_name}'})
        return resp.status_code

    def delete_folder(self, dir_name):
        resp = requests.delete(self.FOLDER_INFO_URL,headers=self.headers, params={'path':f'disk:/{dir_name}'})
        return resp.status_code

token = 'укажите токен'
if __name__ == '__main__':
    ya = YaUploader ( token )
    # pprint(ya.file_get())
    # pprint(ya.folder_info('test')) # получить информацию о существовании папки
    # print(ya.create_folder('test')) # создать папку
    print(ya.delete_folder('test')) # удалить папку