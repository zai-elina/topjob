from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from .models import *
from jobs.models import Company
from .forms import *
from jobs.jobforms import CompanyForm,SearchForm

class PostView(View):
    def get(self, request,slug):
        context={}
        company = Company.objects.get(slug=slug)
        posts = Post.objects.filter(company=company)
        context['company'] = company
        context['posts'] = posts

        return render(request, 'company-blog-list.html', context)



class PostDetail(View):
    def get(self, request, slug_company,slug_post):
        context={}
        company = Company.objects.get(slug=slug_company)
        post = Post.objects.get(slug=slug_post)
        comments = Comment.objects.filter(post=post,parent=None)
        context['comments'] = comments
        context['company'] = company
        context['post']=post
        context['form'] = CommentForm()

        return render(request, 'company-blog-detail.html', context)



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user.company
            obj.save()
            messages.success(request,'Пост успешно создан')
            return redirect('company-blog-detail',obj.company.slug,obj.slug)
        else:
            messages.error(request,'Ошибка заполнения')
            context = {'form':form}
            return render(request,'post_form.html',context)
    if request.method == 'GET':
        form = PostForm()
        context = {'form':form}
        return render(request,'post_form.html',context)

    return render(request,'post_form.html',{})


def company_blogs(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data.get('title')

            company_list = Company.objects.filter(title__icontains=search)

            data = []
            if len(company_list) > 0:
                for item in company_list:
                    val = {
                        'title': item.title,
                        'logo': item.companyLogo.url,
                        'slug': item.slug,
                        'posts': item.post_set.count()
                    }
                    data.append(val)
            return JsonResponse({'data': data}, status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        context = {}
        company_list = Company.objects.all().annotate(num_post=Count('post')).order_by('-num_post')
        context['company_list'] = company_list
        form = SearchForm()
        context['form'] = form


    return render(request, 'company-blogs.html', context)

@login_required
def post_delete(request,slug_company,slug):
    Post.objects.get(slug=slug).delete()
    messages.success(request, 'Пост удалён')
    return redirect('company-blog-list', slug_company)

@login_required
def post_edit(request,slug_company,slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            if 'image' in request.FILES:
                obj.image = request.FILES['image']
            obj.save()
            messages.success(request, 'Изменения внесены')
            return redirect('company-blog-detail',slug_company,obj.slug)
        else:
            messages.error(request, 'Ошибка заполнения')
            context = {'form': form}
            return render(request, 'post_form.html', context)
    if request.method == 'GET':
        form = PostForm(instance=post)
        context = {'form': form}
        return render(request, 'post_form.html', context)

    return render(request, 'post_form.html', {})

@login_required
def add_comment(request,slug_company,slug_post):
    post = Post.objects.get(slug=slug_post)
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.post = post
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()

            obj.parent = parent_obj
            obj.save()
            name = request.user.first_name
            return JsonResponse({'name':name},status=200)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)


    return redirect('company-blog-detail',slug_company,slug_post)


@login_required
def add_reply_comment(request,slug_company,slug_post):
    post = Post.objects.get(slug=slug_post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.post = post
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()

            obj.parent = parent_obj
            obj.save()
            return redirect('company-blog-detail',slug_company,slug_post)
        else:
            return redirect('company-blog-detail',slug_company,slug_post)


    return redirect('company-blog-detail',slug_company,slug_post)



@login_required
def company_edit(request,slug):
    company = Company.objects.get(slug=slug)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES,instance=company)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            if 'image' in request.FILES:
                obj.image = request.FILES['image']
            obj.save()
            messages.success(request, 'Изменения внесены')
            return redirect('company-blog-list',slug)
        else:
            messages.error(request, 'Ошибка заполнения')
            context = {'form': form}
            return render(request, 'create-company.html', context)
    if request.method == 'GET':
        form = CompanyForm(instance=company)
        context = {'form': form}
        return render(request, 'create-company.html', context)

    return render(request, 'create-company.html', {})