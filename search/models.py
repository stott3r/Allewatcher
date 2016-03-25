# -*- coding: utf-8 -*-
# python imports
import re
# django imports
from django.db import models
# packages imports
from django.utils import timezone


class Category(models.Model):

    category_id = models.DecimalField(verbose_name='id kategorii', max_digits=6, decimal_places=0)
    category_name = models.CharField(verbose_name='nazwa kategorii', max_length=100)

    def __str__(self):
        return 'Lista kategorii'

# creates list of choices for Search.category


def list_creator():
    database = Category.objects.all()
    category_list = []
    for entry in database:
        tuples = (entry.category_id, entry.category_name)
        category_list.append(tuples)
    return category_list

final_list = list_creator()


class Search(models.Model):
    mail = models.CharField(verbose_name='Email', max_length=100)
    phrase = models.CharField(verbose_name='Czego szukasz?', max_length=150)
    end_date = models.DateTimeField(verbose_name="Data końcowa", blank=True, null=True)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=timezone.now)
    category = models.DecimalField(verbose_name='Kategoria', max_digits=6,
                                   decimal_places=0, choices=final_list, default=None)
    # for now search engine don't use search_interval yet
    search_interval = models.CharField(verbose_name='Czas wystawienia', max_length=5, default='24h')

    def __str__(self):
        return '%s, %s' % (self.mail, self.phrase)


    class Meta:
        verbose_name = "Wyszukanie"
        verbose_name_plural = "Wyszukania"
