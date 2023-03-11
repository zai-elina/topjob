from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('users/create/',views.create_resume, name='create-resume'),
    path('users/view/<slug:slug>/', views.resume_detail, name='resume-detail'),
    path('users/view/<slug:slug>/<int:pk>/delete-exp', views.delete_exp, name='delete-exp'),
    path('users/view/<slug:slug>/<int:pk>/delete-ed', views.delete_ed, name='delete-ed'),
    path('forgot-password/',views.forgot_password,name='forgot'),
]