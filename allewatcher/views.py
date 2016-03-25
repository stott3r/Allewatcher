# django imports
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
# app imports
from allewatcher.forms import *


def main(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            human = True  # captcha
            email = 'bartlomiej.strzyga@gmail.com'  # address that will receive contact form outputs

            contact_email = form.cleaned_data['contact_email']
            contact_name = form.cleaned_data['contact_name']
            contact_content = form.cleaned_data['contact_content']

            email_subject = 'AlleWatcher - Kontakt'
            email_body = render_to_string('contact_email.txt', {contact_email: 'contact_email',
                                                                contact_name: 'contact_name',
                                                                contact_content: 'contact_content'})
            email_bodyhtml = render_to_string('contact_email.html', {contact_email: 'contact_email',
                                                                     contact_name: 'contact_name',
                                                                     contact_content: 'contact_content'})
            send_mail(email_subject, email_body, 'allewatcher@gmail.com',
                      [email], fail_silently=False, html_message=email_bodyhtml)

            return HttpResponseRedirect('#kontakt')
    else:
        form = ContactForm()
    args['form'] = form

    return render_to_response('home.html', args)
