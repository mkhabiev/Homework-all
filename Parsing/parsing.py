import requests
from bs4 import BeautifulSoup
import csv

CSV = 'anime.csv'
HOST = 'http://www.ts.kg/'
URL = 'http://www.ts.kg/category/anime/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
    'application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    '86.0.4240.75 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='show')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div', class_='show-title').get_text(strip=True),
                'link_movie': HOST + item.find('div', class_='show-title').find('a').get('href'),
                'anime_img': HOST + item.find('div', class_='image').find('img').get('src')
            }
        )
    return anime

def save_anime(items, path):
    with open(path, 'w', newline_='') as file:
        writer = csv.writer(file, delimeter=';')
        writer.writerow(['Название аниме', 'Ссылка на аниме', 'Постер'])
        for item in items:
            writer.writerow([item['title'], item['link_movie'], item['anime_img']])

def parser():
    PAGE = input('Введите количество страниц для парсинга: ')
    PAGE = int(PAGE.strip())
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(1, PAGE):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={'page': page})
            anime.extend(get_content(html.text))
            save_anime(anime, CSV)
        pass
    else:
        print('ErrorMacro')

parser()