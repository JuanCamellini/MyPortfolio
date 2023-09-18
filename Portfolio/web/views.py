from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                'from ' + name + ' subject: ' + subject,
                f'Name: {name}\nEmail: {email}\n\n{message}',
                'settings.EMAIL_HOST_USER',  # Remitente
                [email],  # Destinatario(s)
                fail_silently=False,
                
            )
            return HttpResponse(f"Thank {name} for your message! We'll get back to you as soon as possible.")
    else:
        form = ContactForm()
    return render(request, 'webApp/index.html', {'form': form})

def portfolioDetails(request):
    return render(request, 'webApp/portfolio-details.html')

def greetings(request):
    return render(request, 'webApp/greetings.html')