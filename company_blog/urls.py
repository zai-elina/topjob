from django.urls import path
from .views import *

urlpatterns = [
    path('company-blog/<slug:slug>/', PostView.as_view() , name='company-blog-list'),
    path('company-blog/<slug:slug_company>/<slug:slug_post>', PostDetail.as_view() , name='company-blog-detail'),
]