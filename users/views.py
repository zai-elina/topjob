from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request,'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались")
            user = form.cleaned_data.get('username')
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

