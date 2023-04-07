from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('users/create/',views.create_resume, name='create-resume'),
    path('users/view/<slug:slug>/', views.resume_detail, name='resume-detail'),
    path('users/view/<slug:slug>/delete', views.resume_delete, name='resume-delete'),
    path('users/view/<slug:slug>/<int:pk>/delete-exp', views.delete_exp, name='delete-exp'),
    path('users/view/<slug:slug>/<int:pk>/delete-education', views.delete_ed, name='delete-ed'),
    path('users/view/<slug:slug>/<int:pk>/edit-education',views.edit_education,name='edit-ed'),
    path('users/view/<slug:slug>/<int:pk>/edit-exp',views.edit_exp,name='edit-exp'),
    path('forgot-password/',views.forgot_password,name='forgot'),
    path('edit-profile/',views.edit_user,name='edit-profile'),
    path('edit-resume/<slug:slug>',views.edit_resume,name='edit-resume'),
]