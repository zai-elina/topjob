from django.shortcuts import render
from .models import *

def home(request):
    jobs_list = Jobs.objects.all()
    jobs_list=jobs_list[:4]

    return render(request, 'index.html', {'jobs':jobs_list})

def job_list(request):
    jobs_list = Jobs.objects.all()
    jobs_list = jobs_list[:20]

    return render(request, 'jobs.html', {'jobs': jobs_list})

def job_detail(request, slug):
    job = Jobs.objects.get(slug=slug)

    return render(request, 'job-detail.html', {'job': job})