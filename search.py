from search.models import *
from django.core.mail import send_mail
from datetime import datetime
from django.template.loader import render_to_string
import django
from allegro import *

django.setup()

class Run:
    def __init__(self):
        self.dbase = Search
        self.entries = self.dbase.objects.all()
        self.mail = 'allewatcher@gmail.com'
        self.allegro = Allegro()
        self.categories = self.allegro.get_categories()

    # checks category id to compare with db entry and get its name
    def category_check(self, category):
        category_name = ''
        for item in self.categories:
            if category == item['id']:
                category_name = item['name']
        return category_name

    # converts auction name to more human friendly, also it helps to create valid auction link
    def title_creator(self, string):
        pltoang_tab = string.maketrans("ąćęłńóśżźĄĆĘŁŃÓŚŻŹ", "acelnoszzACELNOSZZ")
        letters_replaced = string.translate(pltoang_tab)
        dashes = '--'
        whites_gone = re.sub('[^A-Za-z0-9 ]+', '', letters_replaced)
        new_name = whites_gone.replace(" ", "-")
        while dashes in new_name:
            if dashes in new_name:
                new_name = new_name.replace("--", "-")
        if new_name[0] == "-":
            new_name = new_name[1:]
        new_name = new_name.lower()
        return new_name

    def engine(self):
        for entry in self.entries:
            email = entry.mail
            phrase = entry.phrase
            interval = entry.search_interval
            result = self.allegro.search(entry.category, phrase, interval)
            category = self.category_check(entry.category)
            for item in result:
                item['name'] = self.title_creator(item['name'])
            email_subject = "AlleWatcher - " + phrase.title() + " w kategorii " + category + "."
            email_body = render_to_string('email.txt', {'phrase': phrase, 'category': category,
                                                        'result': result})
            email_bodyhtml = render_to_string('email.html', {'phrase': phrase, 'category': category,
                                                             'result': result})
            send_mail(email_subject, email_body, 'allewatcher@gmail.com',
                      [email], fail_silently=False, html_message=email_bodyhtml)

a = Run()
a.engine()
