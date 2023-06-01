import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.views.generic.base import View
from .forms import UploadFileForm

from .models import *
from jobs.models import Applicant


@login_required
def chat_message(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('-timestamp')
    context = {
        'threads': threads,
        "form":UploadFileForm
    }
    return render(request, 'chat.html', context)


def create_chat(request,user_1,user_2):
    first_user = User.objects.get(id=user_1)
    second_user = User.objects.get(id=user_2)
    Thread.objects.create(first_person=first_user,second_person=second_user)
    return redirect('chat')

class UploadFileView(View):
    def post(self, request, thread):
        # Получаем загруженный файл из POST-запроса
        uploaded_file = request.FILES['file']

        thread_obj = Thread.objects.get(id=thread)
        ChatMessage.objects.create(thread=thread_obj, user=request.user, message_file=uploaded_file)
        return redirect('chat')