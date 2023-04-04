from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .jobforms import *
from django.contrib.auth.decorators import login_required

def searching(search,type,region):
    jobs = []
    if len(search.split()) > 1:
        search_list = search.split()
        val_list = []
        for i in search_list:
            if (type != '' and region != ''):
                result = Jobs.objects.filter(Q(title__icontains=i) | Q(company__title__icontains=search), type=type,
                                       region=region)
            elif (type != ''):
                result = Jobs.objects.filter(Q(title__icontains=i) | Q(company__title__icontains=search), type=type)
            elif (region != ''):
                result = Jobs.objects.filter(Q(title__icontains=i) | Q(company__title__icontains=search),
                                       region=region)
            else:
                result = Jobs.objects.filter(Q(title__icontains=i) | Q(company__title__icontains=search))
            for j in result:
                val_list.append(j)
        [jobs.append(i) for i in val_list if i not in jobs]
        return jobs
    else:
        if (type != '' and region != ''):
            jobs_list = Jobs.objects.filter(Q(title__icontains=search) | Q(company__title__icontains=search), type=type,
                                       region=region)
        elif (type != ''):
            jobs_list = Jobs.objects.filter(Q(title__icontains=search) | Q(company__title__icontains=search), type=type)
        elif (region != ''):
            jobs_list = Jobs.objects.filter(Q(title__icontains=search) | Q(company__title__icontains=search),
                                       region=region)
        else:
            jobs_list = Jobs.objects.filter(Q(title__icontains=search) | Q(company__title__icontains=search),)
        return jobs_list

def home(request):
    form = SearchForm()
    context = {}

    jobs_list = Jobs.objects.all()
    context['jobs_count'] = len(jobs_list)
    users = User.objects.all()
    company = Company.objects.all()
    jobs_list=jobs_list[:4]

    context['jobs'] = jobs_list
    context['users'] = len(users)
    context['company'] = len(company)


    context['technology'] = Category.objects.get(title = 'IT профессии')
    context['service'] = Category.objects.get(title='Сервис и туризм')
    context['economy'] = Category.objects.get(title='Экономика')
    context['management'] = Category.objects.get(title='Менеджмент (управление)')
    context['jurisprudence'] = Category.objects.get(title='Юриспруденция')
    context['advertising'] = Category.objects.get(title='Маркетинг, реклама и PR')

    context['form'] = form

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')
            type = form.cleaned_data.get('type')
            region = form.cleaned_data.get('region')

            context['jobs'] = searching(search, type, region)

            return render(request, 'jobs.html', context)
        else:
            messages.error(request,'Ошибка запроса')
            context['form'] = form
            return render(request, 'index.html', context)

    return render(request, 'index.html', context)



def job_list(request):
    form = SearchForm()
    context={}
    jobs_list = Jobs.objects.order_by('dateCreated')

    context['form'] = form
    context['jobs'] = jobs_list;

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')
            type = form.cleaned_data.get('type')
            region = form.cleaned_data.get('region')

            context['jobs'] = searching(search,type,region)

            return render(request, 'jobs.html', context)
        else:
            messages.error(request, 'Ошибка запроса')
            context['form'] = form
            return render(request, 'jobs.html', context)


    return render(request, 'jobs.html', context)

def job_detail(request, slug):
    job = Jobs.objects.get(slug=slug)

    return render(request, 'job-detail.html', {'job': job})

def category_detail(request, slug):
    form = SearchForm()
    category =  Category.objects.get(slug=slug)
    context = {}

    jobs = Jobs.objects.filter(category__slug=slug)[:20]
    context['jobs'] = jobs
    context['category'] = category
    context['form'] = form

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')
            type = form.cleaned_data.get('type')
            region = form.cleaned_data.get('region')

            context['jobs'] = searching(search,type,region)
            return render(request, 'category-detail.html', context)
        else:
            messages.error(request,'Ошибка запроса')
            context['form'] = form
            return render(request, 'category-detail.html', context)

    return render(request, 'category-detail.html', context)

def category_list(request):
    categ_list = Category.objects.all()

    return render(request, 'category-list.html', {'category_list': categ_list})


@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request,'Компания добавлена')
            return redirect('profile')
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'create-company.html',context)
    if request.method == 'GET':
        form = CompanyForm()
        context = {'form':form}
        return render(request,'create-company.html',context)

    return render(request,'create-resume.html',{})

@login_required
def create_job(request):
    if not Company.objects.filter(user=request.user):
        return redirect('create-company')