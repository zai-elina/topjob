from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('profile/',views.profile, name='profile'),
    path('users/create/',views.create_resume, name='create-resume'),
    path('users/delete/',views.delete_user, name='delete-user'),
    path('users/view/<slug:slug>/', views.resume_detail, name='resume-detail'),
    path('users/view/<slug:slug>/delete', views.resume_delete, name='resume-delete'),
    path('users/view/<slug:slug>/<int:pk>/delete-exp', views.delete_exp, name='delete-exp'),
    path('users/view/<slug:slug>/<int:pk>/delete-education', views.delete_ed, name='delete-ed'),
    path('users/view/<slug:slug>/<int:pk>/edit-education',views.edit_education,name='edit-ed'),
    path('users/view/<slug:slug>/<int:pk>/edit-exp',views.edit_exp,name='edit-exp'),
    path('forgot-password/',views.forgot_password,name='forgot'),
    path('edit-profile/',views.edit_user,name='edit-profile'),
    path('edit-resume/<slug:slug>',views.edit_resume,name='edit-resume'),
    path('add_to_favorites/<int:job_id>', views.add_to_favorites, name='add_to_favorites'),
    path('delete_in_favorites/<int:job_id>', views.delete_in_favorites, name='delete_in_favorites'),
]