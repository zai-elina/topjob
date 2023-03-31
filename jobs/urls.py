from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('jobs/', views.job_list, name='job-list'),
    path('jobs/<slug:slug>/', views.job_detail, name='job-detail'),
    path('category-list/',views.category_list,name='category-list'),
    path('jobs/category/<slug:slug>/',views.category_detail,name='category-detail'),
]