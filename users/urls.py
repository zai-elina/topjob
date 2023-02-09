from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('users/create/',views.create_resume, name='create-resume'),
    path('users/view/<slug:slug>/', views.ResumeDetailView.as_view(), name='resume-detail'),
]