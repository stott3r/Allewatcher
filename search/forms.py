# -*- coding: utf-8 -*-
# django imports
from django import forms
# packages imports
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# app imports
from search.models import *


class FreeForm(forms.ModelForm):
    mail = forms.EmailField(required=True, label='Email')
# crispy forms additional info

    def __init__(self, *args, **kwargs):
        super(FreeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'search'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = '/search/free/'
        self.helper.add_input(Submit('submit', 'Obserwuj'))

# labels as placeholders
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''

    class Meta:
        model = Search
        fields = ('mail', 'phrase', 'category')
