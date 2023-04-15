from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .email_func import WelcomeEmail,sendEmail, ForgotPassword
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime
from django.db.models import Q

from jobs.models import Applicant,Jobs


from jobs.models import Company


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request,'register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()

            if 'image' in request.FILES:
                profile = Profile.objects.create(
                    user=user,
                    kind=form.cleaned_data['kind'],
                    image=request.FILES['image'],
                )
            else:
                profile = Profile.objects.create(
                    user=user,
                    kind=form.cleaned_data['kind'],
                )

            profile.save()

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



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                if not User.objects.filter(username=username):
                    messages.error(request, 'Пользователь с введенным логином не существует')
                else:
                    messages.error(request, 'Неправильный пароль')
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, 'Ошибка ввода')
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


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

@login_required
def edit_user(request):
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            profile = Profile.objects.get(user=obj.user)
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
                profile.save()
            obj.save()
            messages.success(request,'Изменения внесены')
            return redirect('profile')
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'edit-profile.html',context)
    if request.method == 'GET':
        form = ProfileChangeForm(instance=request.user)
        context = {'form':form}
        return render(request,'edit-profile.html',context)

    return render(request,'edit-profile.html',{})


@login_required
def delete_user(request):
    try:
        u = User.objects.get(username = request.user)
        u.delete()
        messages.success(request, "Профиль удален")
    except User.DoesNotExist:
        messages.error(request, "Пользователя нет")
        return redirect('login')

    return redirect('login')



@login_required
def edit_resume(request,slug):
    instance = Resume.objects.get(slug=slug)
    if request.method == 'POST':
        form = ResumeEditForm(request.POST,instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_updated = timezone.now()
            obj.save()
            messages.success(request,'Изменения внесены')
            return redirect('resume-detail',slug=slug)
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'edit-resume.html',context)
    if request.method == 'GET':
        form = ResumeEditForm(instance=instance)
        context = {'form':form}
        return render(request,'edit-resume.html',context)

    return render(request,'edit-resume.html',{})

@login_required
def resume_detail(request,slug):
    obj = Resume.objects.get(slug=slug)

    educations = Education.objects.filter(resume=obj)
    experiences = Experience.objects.filter(resume=obj)
    context ={}
    context['object'] = obj
    context['educations']=educations
    context['experiences'] = experiences

    if request.method == "POST" and 'btnEducation' in request.POST:
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


    if request.method == "POST" and 'btnExperience' in request.POST:
        exp_form = ExperienceForm(request.POST)
        if exp_form.is_valid():
            new = exp_form.save(commit=False)
            new.resume = obj
            new.save()

            messages.success(request,'Резюме обновлено')
            return redirect('resume-detail',slug=slug)
        else:
            messages.error(request,'Ошибка запроса')
            context['exp_form']=exp_form
            return render(request,'resume-detail.html',context)



    if request.method == 'GET':
        edu_form = EducationForm()
        context['edu_form'] = edu_form
        exp_form = ExperienceForm()
        context['exp_form'] = exp_form
        return render(request, 'resume-detail.html', context)



    return render(request, 'resume-detail.html', context)

@login_required
def resume_delete(request,slug):
    obj = Resume.objects.filter(slug=slug)
    obj.delete()
    messages.success(request, 'Резюме удалено')
    return redirect('profile')

@login_required
def delete_exp(request,slug,pk):
    exp = Experience.objects.filter(pk=pk)
    exp.delete()
    messages.success(request, 'Опыт удален')
    return redirect('resume-detail',slug=slug)

@login_required
def delete_ed(request,slug,pk):
    ed = Education.objects.filter(pk=pk)
    ed.delete()
    messages.success(request, 'Образование удалено')
    return redirect('resume-detail',slug=slug)

@login_required
def edit_education(request,slug,pk):
    ed = Education.objects.get(pk=pk)
    if request.method == 'POST':
        form = EducationForm(request.POST,instance=ed)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request,'Изменения внесены')
            return redirect('resume-detail',slug=slug)
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'edu_form':form}
            return render(request,'edit-education.html',context)
    if request.method == 'GET':
        form = EducationForm(instance=ed)
        context = {'edu_form':form}
        return render(request,'edit-education.html',context)

    return render(request,'edit-education.html',{})

@login_required
def edit_exp(request,slug,pk):
    ex = Experience.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST,instance=ex)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request,'Изменения внесены')
            return redirect('resume-detail',slug=slug)
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'edit-exp.html',context)
    if request.method == 'GET':
        form = ExperienceForm(instance=ex)
        context = {'form':form}
        return render(request,'edit-exp.html',context)

    return render(request,'edit-exp.html',{})


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


@login_required
def add_to_favorites(request,job_id):
    job = Jobs.objects.get(id=job_id)
    Favorite.objects.create(job=job, user=request.user)
    context={}
    context['job'] = job
    context['applicants'] = len(Applicant.objects.filter(job=job))
    context['favorite'] = len(Favorite.objects.filter(job=job))

    messages.success(request, 'Вакансия сохранена')

    return render(request, "job-detail.html",context)

@login_required
def delete_in_favorites(request,job_id):
    job = Jobs.objects.get(id=job_id)
    Favorite.objects.filter(job=job, user=request.user).delete()

    context = {}
    context['job'] = job
    context['applicants'] = len(Applicant.objects.filter(job=job))
    context['favorite'] = len(Favorite.objects.filter(job=job))

    messages.success(request, 'Вакансия удалена из сохраненных')

    return render(request, "job-detail.html",context)



@login_required
def favorites_job(request):
    fav = Favorite.objects.filter(user=request.user)
    context={}
    if fav:
        context['favorites'] = fav

    return render(request, 'favorite-job.html', context)

@login_required
def applies_job(request):
    appl = Applicant.objects.filter(user=request.user)
    context={}
    if appl:
        context['applies'] = appl

    return render(request, 'apply-job.html', context)


def split_search(val_list,search,region,city,skills):
    if (region != '' and city != '' and skills != ''):
        result = Resume.objects.filter(profession__icontains=search, region=region,
                                       city__icontains=city, skills__icontains=skills)
    elif (region != '' and city != ''):
        result = Resume.objects.filter(profession__icontains=search, region=region, city__icontains=city)
    elif (city != '' and skills != ''):
        result = Resume.objects.filter(profession__icontains=search, skills__icontains=skills, city__icontains=city)
    elif (region != '' and skills != ''):
        result = Resume.objects.filter(profession__icontains=search, region=region, skills__icontains=skills)
    elif (skills != ''):
        result = Resume.objects.filter(profession__icontains=search, skills__icontains=skills)
    elif (region != ''):
        result = Resume.objects.filter(profession__icontains=search, region=region)
    elif (city != ''):
        result = Resume.objects.filter(profession__icontains=search, city__icontains=city)
    else:
        result = Resume.objects.filter(profession__icontains=search)
    for j in result:
        val_list.append(j)
    return val_list

def searching(search,region,city,skills):
    resume_list = []
    if len(search.split()) > 1 and len(skills.split()) > 1:
        search_list = search.split()
        skills_list =skills.split()
        val_list = []
        for i in search_list:
            for j in skills_list:
                val_list = split_search(val_list,i,region,city,j)

        [resume_list.append(i) for i in val_list if i not in resume_list]
        return resume_list
    elif len(search.split()) > 1:
        search_list = search.split()
        val_list = []
        for i in search_list:
            val_list = split_search(val_list, i, region, city, skills)

        [resume_list.append(i) for i in val_list if i not in resume_list]
        return resume_list
    elif len(skills.split()) > 1:
        skills_list =skills.split()
        val_list = []
        for i in skills_list:
            val_list = split_search(val_list, search, region, city, i)
        [resume_list.append(i) for i in val_list if i not in resume_list]
        return resume_list
    else:
        if (region != '' and city !='' and skills!=''):
            resume_list = Resume.objects.filter(profession__icontains=search, region=region,
                                   city__icontains=city,skills__icontains=skills)
        elif (region != '' and city !=''):
            resume_list = Resume.objects.filter(profession__icontains=search, region=region,city__icontains=city)
        elif (city !='' and skills!=''):
            resume_list = Resume.objects.filter(profession__icontains=search, skills__icontains=skills,city__icontains=city)
        elif (region !='' and skills!=''):
            resume_list = Resume.objects.filter(profession__icontains=search, region=region,skills__icontains=skills)
        elif (skills!=''):
            resume_list = Resume.objects.filter(profession__icontains=search, skills__icontains=skills)
        elif (region !=''):
            resume_list = Resume.objects.filter(profession__icontains=search, region=region)
        elif (city!=''):
            resume_list = Resume.objects.filter(profession__icontains=search,city__icontains=city)
        else:
            resume_list = Resume.objects.filter(profession__icontains=search)
        return resume_list

def resume_list(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchFormResume(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('profession')
            region = form.cleaned_data.get('region')
            city = form.cleaned_data.get('city')
            skills = form.cleaned_data.get('skills')

            resume_list = searching(search, region, city, skills)

            data = []
            if len(resume_list) > 0:
                for item in resume_list:
                    val = {
                        'profession':item.profession,
                        'region':item.suburb,
                        'city':item.city,
                        'slug': item.slug,
                        'image':item.user.profile.image.url,
                        }
                    data.append(val)
            return JsonResponse({'data':data},status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        resume = Resume.objects.all().order_by('date_created')
        context = {}
        context['resume_list'] = resume
        form = SearchFormResume()
        context['form'] = form


    return render(request, 'resume-list.html', context)

@login_required
def delete_company(request):
    company = Company.objects.filter(user=request.user)
    company.delete()
    messages.success(request, 'Компания удалена')

    return redirect('profile')