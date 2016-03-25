from allegro import *
from search.models import Category
from search.models import Search
from datetime import datetime
# module executing every 12 hours
# creates tuple with category choices and saves it in database


def choices():
    allegro = Allegro()
    choice = allegro.get_categories()
    comma = ","
    for item in choice:
        if item['parent'] == 0:
            name = item['name']
            if comma in name:
                name = name.replace(",", " -")
            entry = Category(category_id=item['id'], category_name=item['name'])
            entry.save()


# checks database entries and deletes old or not activated searchings


def check():
    dbase = Search
    dbase_all = dbase.objects.all()
    date = datetime.now()
    for entry in dbase_all:
        if entry.end_date is not None:
            if entry.end_date < date:
                entry.delete()
        else:
            if entry.key_expires < date:
                    entry.delete()

a = choices()
b = check()
