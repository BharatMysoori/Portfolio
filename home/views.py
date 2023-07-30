from django.shortcuts import render, HttpResponse,redirect
from .models import *
from portfolio.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from email.message import EmailMessage
import smtplib
# Create your views here.

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login("tempomail736@gmail.com",'cqqkybllyvpryekd')

def home(request):
    print(request.method=='POST')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']
        message = 'Subject: Name:{}\n\nEmail:{}\n\nSubject:{}\n\nMessage:{}'.format(name,email,subject, msg)
        print("MESSAGE:",message)
        contact = Contact(name=name, email=email, subject=subject, message=message)
        print("Contact:",contact,name,email)
        contact.save()
        """send_mail(subject,message,EMAIL_HOST_USER,[email],fail_silently=False)
        print("email hostusre",EMAIL_HOST_USER,email)"""
        server.sendmail('tempomail736@gmail.com','mysoori.bharat@gmail.com',message)
        
        return redirect('home')
    

    
    return render(request, 'home.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    #contact form database
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = models.Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        
        
    return render(request, 'home.html')

