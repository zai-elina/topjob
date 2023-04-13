from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


@login_required
def chat_message(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    context = {
        'threads': threads
    }
    return render(request, 'chat.html', context)


def create_chat(request,user_1,user_2):
    first_user = User.objects.get(id=user_1)
    second_user = User.objects.get(id=user_2)
    Thread.objects.create(first_person=first_user,second_person=second_user)
    return redirect('chat')