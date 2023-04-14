from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from .jobforms import *
from django.contrib.auth.decorators import login_required

from django.apps import apps

from users.models import Favorite

Resume = apps.get_model('users', 'Resume')
Education = apps.get_model('users', 'Education')
Experience = apps.get_model('users', 'Experience')



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

    jobs_list = Jobs.objects.filter(filled=False)
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


    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')
            type = form.cleaned_data.get('type')
            region = form.cleaned_data.get('region')

            jobs = searching(search, type, region)
            data = []
            if len(jobs) > 0:
                for item in jobs:
                    val = {
                        'title':item.title,
                        'city':item.city,
                        'logo':item.company.companyLogo.url,
                        'slug':item.slug,
                        'salary':item.salary,
                        'type':item.type,
                        'company':item.company.title
                    }
                    data.append(val)
            return JsonResponse({'data':data},status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = SearchForm()
        jobs = Jobs.objects.filter(filled=False).order_by('dateCreated')
        context['form'] = form
        context['jobs'] = jobs

    return render(request, 'jobs.html', context)

def job_detail(request, slug):
    job = Jobs.objects.get(slug=slug)
    context ={}
    context['applicants'] = len(Applicant.objects.filter(job=job))
    context['favorite'] = len(Favorite.objects.filter(job=job))
    context['job'] = job

    return render(request, 'job-detail.html', context)

def category_detail(request, slug):
    form = SearchForm()
    context = {}

    #
    #
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         search = form.cleaned_data.get('title')
    #         type = form.cleaned_data.get('type')
    #         region = form.cleaned_data.get('region')
    #
    #         context['jobs'] = searching(search,type,region)
    #         return render(request, 'category-detail.html', context)
    #     else:
    #         messages.error(request,'Ошибка запроса')
    #         context['form'] = form
    #         return render(request, 'category-detail.html', context)


    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')
            type = form.cleaned_data.get('type')
            region = form.cleaned_data.get('region')
            category = Category.objects.get(slug=slug)

            jobs = searching(search, type, region)
            data = []
            if len(jobs) > 0:
                for item in jobs:
                    if item.category.slug == category.slug:
                        val = {
                            'title':item.title,
                            'city':item.city,
                            'logo':item.company.companyLogo.url,
                            'slug':item.slug,
                            'salary':item.salary,
                            'type':item.type,
                            'company':item.company.title
                        }
                        data.append(val)
            return JsonResponse({'data':data},status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = SearchForm()
        category = Category.objects.get(slug=slug)
        jobs = Jobs.objects.filter(category__slug=slug)
        context['jobs'] = jobs
        context['category'] = category
        context['form'] = form

    return render(request, 'category-detail.html', context)

def category_list(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')

            categ_list = Category.objects.filter(title__icontains=search)

            data = []
            if len(categ_list) > 0:
                for item in categ_list:
                    val = {
                        'title':item.title,
                        'logo':item.categoryImage.url,
                        'slug':item.slug,
                        'description':item.description,
                        }
                    data.append(val)
            return JsonResponse({'data':data},status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        context = {}
        categ_list = Category.objects.all()
        context['category_list'] = categ_list
        form = SearchForm()
        context['form'] = form

    return render(request, 'category-list.html', context)


@login_required
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request,'Компания добавлена')
            return redirect('create-job')
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'create-company.html',context)
    if request.method == 'GET':
        form = CompanyForm()
        context = {'form':form}
        return render(request,'create-company.html',context)

    return render(request,'create-company.html',{})

@login_required
def create_job(request):
    if not Company.objects.filter(user=request.user):
        return redirect('create-company')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            company = Company.objects.get(user=request.user)
            obj.datePosted = timezone.now()
            obj.company = company
            obj.save()
            messages.success(request,'Вакансия добавлена')
            return redirect('published-jobs')
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'create-job.html',context)
    if request.method == 'GET':
        form = JobForm()
        context = {'form':form}
        return render(request,'create-job.html',context)
    return render(request, 'create-job.html', {})


@login_required
def edit_job(request,slug):
    job =Jobs.objects.get(slug=slug)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'Изменения внесены')
            return redirect('published-jobs')
        else:
            messages.error(request, 'Ошибка заполнения')
            context = {'form': form}
            return render(request, 'edit-job.html', context)
    if request.method == 'GET':
        form = JobForm(instance=job)
        context = {'form': form}
        return render(request, 'edit-job.html', context)

    return render(request, 'edit-job.html', {})

@login_required
def published_jobs(request):
    company = Company.objects.get(user=request.user)
    jobs = Jobs.objects.filter(company=company)

    for job in jobs:
        if job.closingDate <= timezone.now().date():
            Jobs.objects.filter(slug=job.slug).delete()

    context={}

    context['jobs'] = jobs
    return render(request, 'published-jobs.html', context)


@login_required
def add_respond(request,slug):
    context={}
    user = request.user
    job= Jobs.objects.get(slug=slug)
    context['job'] = job

    Applicant.objects.create(user=user,job=job)
    messages.success(request, 'Вы откликнулись')
    context['applicants'] = len(Applicant.objects.filter(job=job))
    context['favorite'] = len(Favorite.objects.filter(job=job))


    return render(request, "job-detail.html",context )

@login_required
def get_applicants(request,slug):
    job = Jobs.objects.get(slug=slug)
    applicants = Applicant.objects.filter(job=job)

    context = {}
    context['applicants'] = applicants
    context['job_title'] = job.title
    context['job_slug'] = job.slug

    return render(request, 'applicants-list.html', context)

@login_required
def delete_job(request,slug):
    job = Jobs.objects.get(slug=slug)
    job.delete()
    return  redirect('published-jobs')

@login_required
def job_filled(request,slug):
    job = Jobs.objects.get(slug=slug)
    job.filled = not job.filled
    job.save()

    return redirect('published-jobs')


def resume_view(request,slug_resume):
    obj = Resume.objects.get(slug=slug_resume)
    educations = Education.objects.filter(resume=obj)
    experiences = Experience.objects.filter(resume=obj)

    context = {}
    context['object'] = obj
    context['educations'] = educations
    context['experiences'] = experiences

    return render(request, 'resume-view.html', context)
