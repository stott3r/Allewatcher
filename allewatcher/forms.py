# -*- coding: utf-8 -*-
# django imports
from django import forms
# packages imports
from captcha.fields import CaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label='Imię i nazwisko')
    contact_email = forms.EmailField(required=True, label='Adres email')
    contact_content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label='Wiadomość'
    )
    captcha = CaptchaField()

# crispy forms additional info
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contact'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Wyślij'))

# labels as placeholders
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
