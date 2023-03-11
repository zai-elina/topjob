from django.shortcuts import render
from .models import Jobs

def home(request):
    jobs_list = Jobs.objects.all()
    jobs_list=jobs_list[:4]

    return render(request, 'index.html', {'jobs':jobs_list})
