from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.edit import FormMixin
from hitcount.models import Hit
from hitcount.views import HitCountDetailView

from .jobforms import *
from django.contrib.auth.decorators import login_required

from django.apps import apps

from users.models import Favorite

from chat.models import Thread

Resume = apps.get_model('users', 'Resume')
Education = apps.get_model('users', 'Education')
Experience = apps.get_model('users', 'Experience')

import django_filters

class JobFilter(django_filters.FilterSet):
    region = django_filters.CharFilter(field_name='region')
    type = django_filters.CharFilter(field_name='type')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    experience = django_filters.CharFilter(field_name='experience')
    salary = django_filters.CharFilter(method='filter_salary')
    class Meta:
        model = Jobs
        fields = [ 'region', 'type', 'category','experience','salary']

    def filter_salary(self, queryset, name, value):
        return queryset.filter(Q(max_salary__gte=value) | Q(min_salary__gte=value))


def job_list(request):
    form = SearchForm()
    context = {}

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')
            salary = form.cleaned_data.get('salary')


            jobs = Jobs.objects.filter(Q(title__icontains=search) | Q(company__title__icontains=search),filled=False)
            job_filter = JobFilter(request.POST, queryset=jobs)
            jobs = job_filter.qs

            data = []
            for item in jobs:
                val = {
                    'title': item.title,
                    'city': item.city,
                    'logo': item.company.companyLogo.url,
                    'slug': item.slug,
                    'max_salary': item.max_salary,
                    'min_salary': item.min_salary,
                    'type': item.type,
                    'company': item.company.title
                }
                data.append(val)

            return JsonResponse({'data': data}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = SearchForm()
        context['form'] = form
        context['jobs'] = Jobs.objects.filter(filled=False).order_by('-dateCreated')

    return render(request, 'jobs.html', context)



def home(request):
    form = SearchForm()
    context = {}

    jobs_list = Jobs.objects.filter(filled=False)
    context['jobs_count'] = len(jobs_list)
    users = User.objects.all()
    company = Company.objects.all()
    jobs_list=jobs_list[:3]

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

            jobs = Jobs.objects.filter(Q(title__icontains=search) | Q(company__title__icontains=search), filled=False)
            job_filter = JobFilter(request.POST, queryset=jobs)
            jobs = job_filter.qs
            context['jobs'] = jobs

            return render(request, 'jobs.html', context)
        else:
            messages.error(request,'Ошибка запроса')
            context['form'] = form
            return render(request, 'index.html', context)

    return render(request, 'index.html', context)



class JobDetailView(FormMixin,HitCountDetailView):
    model = Jobs
    template_name = 'job-detail.html'
    context_object_name = 'job'
    slug_url_kwarg = 'slug'
    form_class = CoverLetterForm
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = self.get_object()
        context['applicants'] = len(Applicant.objects.filter(job=job))
        context['favorite'] = len(Favorite.objects.filter(job=job))
        context['form'] = self.get_form()
        latest_hit = Hit.objects.filter(hitcount__object_pk=self.get_object().pk)
        user_set = set()
        user_list = []
        for hit in latest_hit:
            user = hit.user.username if hit.user else 'Anonymous'
            if user != 'Anonymous' and user not in user_set:
                user_set.add(user)
                user_list.append(User.objects.get(username=user))
        context['user_hits'] = user_list
        return context


def category_detail(request, slug):
    form = SearchForm()
    context = {}

    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')
            category = Category.objects.get(slug=slug)

            jobs = Jobs.objects.filter(Q(title__icontains=search) | Q(company__title__icontains=search), filled=False)
            job_filter = JobFilter(request.POST, queryset=jobs)
            jobs = job_filter.qs

            data = []
            for item in jobs:
                if item.category.slug == category.slug:
                    val = {
                        'title': item.title,
                        'city': item.city,
                        'logo': item.company.companyLogo.url,
                        'slug': item.slug,
                        'max_salary': item.max_salary,
                        'min_salary': item.min_salary,
                        'type': item.type,
                        'company': item.company.title
                    }
                    data.append(val)

            return JsonResponse({'data': data}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = SearchForm()
        category = Category.objects.get(slug=slug)
        jobs = Jobs.objects.filter(category__slug=slug,filled=False).order_by('-dateCreated')
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
    jobs = Jobs.objects.filter(company=company).order_by("-dateCreated")

    for job in jobs:
        if job.closingDate <= timezone.now().date():
            Jobs.objects.filter(slug=job.slug).delete()

    context={}

    context['jobs'] = jobs
    return render(request, 'published-jobs.html', context)




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
    messages.success(request, 'Вакансия удалена')
    return  redirect('published-jobs')

@login_required
def job_filled(request,slug):
    job = Jobs.objects.get(slug=slug)
    job.filled = not job.filled
    job.save()
    return redirect('published-jobs')


class ResumeDetailView(HitCountDetailView):
    model = Resume
    template_name = 'resume-view.html'
    context_object_name = 'object'
    slug_url_kwarg = 'slug_resume'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        educations = Education.objects.filter(resume=obj)
        experiences = Experience.objects.filter(resume=obj)
        context['educations'] = educations
        context['experiences'] = experiences
        return context


@login_required
def delete_apply(request,slug,apply_id,):
    Applicant.objects.filter(id=apply_id).delete()
    messages.success(request, 'Соискатель удален')
    return redirect('get-applicants',slug)


@login_required
def send_cover_letter(request,slug):
    context = {}
    user = request.user
    job = Jobs.objects.get(slug=slug)
    context['job'] = job
    context['applicants'] = len(Applicant.objects.filter(job=job))
    context['favorite'] = len(Favorite.objects.filter(job=job))

    if request.method == 'POST':
        form = CoverLetterForm(request.POST)
        if form.is_valid():
            Applicant.objects.create(user=user, job=job)

            first_user = User.objects.get(id=user.id)
            second_user = User.objects.get(id=job.company.user.id)
            if not Thread.objects.filter(first_person=first_user, second_person=second_user).first() and not Thread.objects.filter(second_person=first_user,first_person=second_user).first():
                thread = Thread.objects.create(first_person=first_user, second_person=second_user)
            else:
                thread = Thread.objects.filter(first_person=first_user, second_person=second_user).first() or Thread.objects.filter(second_person=first_user,first_person=second_user).first()


            obj = form.save(commit=False)
            text = form.cleaned_data.get('message_text')
            obj.message_text = f"Отклик на вакансию \"{job.title}\""+ '\n' + text
            obj.thread = thread
            obj.user = user
            obj.save()

            messages.success(request, 'Вы откликнулись')
            return redirect('chat')
        else:
            messages.error(request, 'Ошибка заполнения')
            context = {'form': form}
            return render(request, "job-detail.html", context)
    else:
        context['form'] = CoverLetterForm()

    return render(request, "job-detail.html", context)


def company_jobs(request,slug):
    company = Company.objects.get(slug=slug)
    jobs = Jobs.objects.filter(company=company)
    context = {}
    context['jobs'] = jobs
    context['company'] = company
    return render(request, "company-jobs.html", context)
