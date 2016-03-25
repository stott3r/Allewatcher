# python imports
import datetime
import hashlib
import random
# django imports
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
# app imports
from search.models import *
from search.forms import FreeForm


def free_search(request):
    args = {}
    args['message'] = 'none'
    args.update(csrf(request))
    if request.POST:
        form = FreeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['mail']
            category = form.cleaned_data['category']
            phrase = form.cleaned_data['phrase']
            salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
            activation_key = hashlib.sha1((salt + email).encode('utf-8')).hexdigest()
            key_expire = datetime.datetime.today() + datetime.timedelta(2)
            new_search = Search(mail=email, phrase=phrase, activation_key=activation_key,
                                    key_expires=key_expire, category=category)
            new_search.save()

            email_subject = 'AlleWatcher - potwierdź obserwację'
            email_body = render_to_string('auth_email.txt', {'phrase': phrase, 'activation_key': activation_key})
            email_bodyhtml = render_to_string('auth_email.html', {'phrase': phrase, 'activation_key': activation_key})

            send_mail(email_subject, email_body, 'allewatcher@gmail.com',
                      [email], fail_silently=False, html_message=email_bodyhtml)

            return HttpResponseRedirect('search_send/')
    else:
        form = FreeForm()
    args['form'] = form
    return render_to_response('search_free.html', args)


def search_send(request):
    return render_to_response('search_send.html')


def search_confirmed(request, activation_key):
    search = get_object_or_404(Search, activation_key=activation_key)
    search.end_date = datetime.datetime.today() + datetime.timedelta(7)
    search.save()
    return render_to_response('search_activated.html')
