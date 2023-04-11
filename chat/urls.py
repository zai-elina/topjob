from django.urls import path
from . import views

urlpatterns = [
    path('chat/<slug:slug>',views.chat_message,name='chat'),
    path('chat-list/',views.chat_list,name='chat-list'),
    path('chat-create/<slug:slug_user1>/<slug:slug_user2>',views.create_chat,name='create-chat'),
]