from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from jobs.models import Company


class PostView(View):
    def get(self, request,slug):
        context={}
        company = Company.objects.get(slug=slug)
        posts = Post.objects.filter(company=company)
        context['company'] = company
        context['posts'] = posts

        return render(request, 'company-blog-list.html', context)