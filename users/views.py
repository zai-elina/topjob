from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import get_template

from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime

from django.conf import settings
from django.views.static import serve
import os

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request,'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Вы успешно зарегистрировались, " + user + " !Пожалуйста, зайдите в свой аккаунт.")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
            context = {'form': form}
            return render(request, 'register.html', context)
    return render(request, 'register.html', {})

@login_required
def profile(request):
    return render(request,'profile.html',{})


@login_required
def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request,'Резюме успешно создано')
            return redirect('profile')
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'create-resume.html',context)
    if request.method == 'GET':
        form = ResumeForm()
        context = {'form':form}
        return render(request,'create-resume.html',context)

    return render(request,'create-resume.html',{})

class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume-detail.html'


def test_email(request):
    email={}
    email['title']='Тестовое сообщение'
    email['subtitle']='Тест для себя'
    email['message'] = 'Сообщение отправлено с помощью Django'

    subject ='[TOPJOB] тест почты'
    from_email = settings.EMAIL_HOST_USER
    to_email = ['8gelina@gmail.com']
    text_content= """
    {}
    {} ,
    Поддержка TOPJOB
    """.format(email['subtitle'],email['message'])
    html_c = get_template('email.html')
    d = {'email':email}
    html_content = html_c.render(d)

    msg =EmailMultiAlternatives(subject,text_content,from_email,to_email)
    msg.attach_alternative(html_content,'text/html')