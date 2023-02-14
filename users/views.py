from django.shortcuts import render, redirect
from django.contrib import messages
from .email_func import WelcomeEmail,sendEmail, ForgotPassword
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request,'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            #отправка email
            to_email = form.cleaned_data.get('email')
            welcome = WelcomeEmail()
            sendEmail(welcome.email,welcome.subject,[to_email])


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

def resume_detail(request,slug):
    obj = Resume.objects.get(slug=slug)

    educations = Education.objects.filter(resume=obj)
    context ={}
    context['object'] = obj
    context['education']=educations

    if request.method == "POST":
        edu_form = EducationForm(request.POST)
        if edu_form.is_valid():
            new = edu_form.save(commit=False)
            new.resume = obj
            new.save()

            messages.success(request,'Резюме обновлено')
            return redirect('resume-detail',slug=slug)
        else:
            messages.error(request,'Ошибка запроса')
            context['edu_form']=edu_form
            return render(request,'resume-detail.html',context)

    if request.method == 'GET':
        edu_form = EducationForm()
        context['edu_form'] = edu_form
        return render(request, 'resume-detail.html', context)

    return render(request, 'resume-detail.html', context)







def forgot_password(request):
    if request.method == "POST":
        form = ForgotForm(request.POST)
        if form.is_valid():
            user_email = request.POST['email'].lower().replace(' ','')

            user = User.objects.get(email= user_email)
            if user is not None:
                new_pass = str(uuid4()).split('-')[4]
                forgot = ForgotPassword(new_pass)

                to_email = user.email
                e_mail = forgot.email()
                sendEmail(e_mail,forgot.subject,[to_email])

                user.set_password(new_pass)
                user.save()

                messages.success(request,'Ваш старый пароль был удалён, мы прислали новый пароль вам на почту')
                return redirect('login')
            else:
                messages.error(request,'Нет пользователя с данной почтой')
                return redirect('home_page')
        else:
            messages.error(request,'Ошибка запроса')
            context = {'form':form}
            return render(request,'forgot.html',context)

    if request.method == "GET":
        form =ForgotForm()
        context = {'form':form}
        return render(request,'forgot.html',context)

    return render(request,'forgot.html',{})