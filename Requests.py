import requests
from pprint import pprint
class MyOpen:
    def __init__(self, path=(input('Введите путь к файлу: ')), method='r'):

        self.path = path
        self.method = method


    def __enter__(self):
        # self.path = input('ведите путь к файлу: ')
        self.file = open(self.path, self.method, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        b = self.file.read()
        # pprint(b)

class MyWrite:

    def __init__(self, path=(input('Введите файл для записи: ')), method='w'):
        self.path = path
        self.method = method


    def __enter__(self):
        self.file = open(self.path, self.method, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
# with open('DE.txt') as DE:   # задать путь к файлу
#     a = DE.read()
# pprint(a)
def translate_it(text, from_lang=input('Введите язык оригинала: '), to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),    # задать язык
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    return ''.join(json_['text'])


if __name__ == '__main__':
    # print(translate_it(a, 'en'))
    with MyOpen() as i:
        result = translate_it(i)
        pprint(result)

    with MyWrite() as write_file:
        write_file.write(result)

    TOKEN = 'AgAAAAAGGrLcAAYbXRZjF_xTQUyxtrkqH8rN7y8'
    URL_UP = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    params = {
        'path': 'app:/File.txt',
        'overwrite': True,
    }
    headers = {
        'Authorization': TOKEN
    }
    resp = requests.get(URL_UP, params=params, headers=headers)
    p = resp.json()
    h = p['href']

    requests.put(h, result.encode('utf-8'))
