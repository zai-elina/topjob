from django.shortcuts import render, redirect
from .models import *


def chat_message(request):
    # obj = ChatRoom.objects.get(slug=slug)
    # context={}
    # context['object'] = obj
    return render(request,'chat.html')

def chat_list(request):
    return render(request,'chat-list.html')

def create_chat(request,slug_user1,slug_user2):
    name='{}+{}'.format(slug_user1,slug_user2)
    obj = ChatRoom.objects.create(name=name)
    return redirect('chat',slug=obj.slug)