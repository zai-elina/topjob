from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import *
from .models import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F, Case, When, Value, BooleanField

class InterviewPlanning(LoginRequiredMixin,ListView):
    model = Interview
    template_name = 'interview_planning.html'
    context_object_name = 'interviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['interviews'] = context['interviews'].filter(user=self.request.user).annotate(
            is_true=Case(
                When(complete=True, then=Value(True)),
                default=Value(False),
                output_field=BooleanField(),
            )
        ).order_by('task_date',F('is_true').desc(nulls_last=True))
        context['count'] = context['interviews'].filter(complete = False).count()

        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['interviews'] = context['interviews'].filter(title__icontains=search_input).order_by('task_date')

        context['search_input'] = search_input
        return context


class InterviewDetail(LoginRequiredMixin,DetailView):
    model = Interview
    context_object_name = 'interview'


class InterviewCreate(LoginRequiredMixin,CreateView):
    form_class = InterviewForm
    model = Interview
    success_url = reverse_lazy('interview-planning')
    template_name = 'interview_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InterviewCreate,self).form_valid(form)


class InterviewEdit(LoginRequiredMixin,UpdateView):
    form_class = InterviewForm
    model = Interview
    success_url = reverse_lazy('interview-planning')
    template_name = 'interview_form.html'


class InterviewDelete(LoginRequiredMixin,DeleteView):
    model = Interview
    context_object_name = 'interview'
    success_url = reverse_lazy('interview-planning')
    template_name = 'interview_confirm_delete.html'

    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)


def interview_complete(request,pk):
    interview =  Interview.objects.get(pk=pk)
    interview.complete = not interview.complete
    interview.save()
    return redirect('interview-planning')