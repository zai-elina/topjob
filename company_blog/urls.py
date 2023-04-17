from django.urls import path
from .views import *

urlpatterns = [
    path('company-blog/<slug:slug>/', PostView.as_view() , name='company-blog-list'),
]