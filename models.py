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


#hello