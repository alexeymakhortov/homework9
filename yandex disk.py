import requests
import os

class YaUploader:
	def __init__(self, file_path: str):
		self.file_path = file_path
	
	def upload(self):
		user_input = input('Введите токен: ')
		header = {'Authorization': None}
		header['Authorization'] = user_input
		
		with open(self.file_path, 'r+b') as f:
			test_file = f.read()  # читаем/записываем данные из файла
		
		_, fname = os.path.split(self.file_path)
		
		response = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path=/{fname}', headers=header)  # в ссылку вставляем название переменной file_name
		
		href = response.json()['href']  # ссылку для загрузки добавляем в переменную
		
		r = requests.put(href, data=test_file)  # загружаем файл на YD, в поле data передаем нашу переменную, где считывали данные из файла
		
		print('Загрузка успешно завершена!')

if __name__ == '__main__':
	uploader = YaUploader('')
	result = uploader.upload()




