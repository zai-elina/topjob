from django.urls import path
from . import views
from .views import UploadFileView

urlpatterns = [
    path('chat/',views.chat_message,name='chat'),
    path('chat-create/<int:user_1>/<int:user_2>',views.create_chat,name='create-chat'),
    path('chat/file/<int:thread>', UploadFileView.as_view(), name='upload_file')
]