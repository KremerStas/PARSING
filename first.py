import requests
from bs4 import BeautifulSoup
from peewee import *

db = SqliteDatabase('films.db')


class Films(Model):
    title = CharField()
    years = CharField()
    country = CharField()
    genre = CharField()

    class Meta:
        database = db


Films.create_table()


for i in range(1, 966):
    if i == 1:
        par = requests.get('http://bestofkinopoisk.com/')
    par = requests.get('http://bestofkinopoisk.com/page/{}'.format(i))
    soup = BeautifulSoup(par.text, 'html.parser')

    for tags in soup.find_all('div', class_='b-content__inline_item-link'):
        if tags.div.attrs:
            continue
        else:
            info = tags.div.string.split(',')
            while len(info) < 3:
                info.insert(1, 'None')
                print(info)
            tl = tags.a.string
            film = Films(title=tl, years=info[0], country=info[1], genre=info[2])
            film.save()
