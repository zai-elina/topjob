from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('jobs/', views.job_list, name='job-list'),
    path('jobs/<slug:slug>/', views.job_detail, name='job-detail'),
    path('category-list/',views.category_list,name='category-list'),
    path('jobs/category/<slug:slug>/',views.category_detail,name='category-detail'),
    path('create-company/',views.create_company,name='create-company'),
    path('create-job/',views.create_job,name='create-job'),
    path('published-jobs/',views.published_jobs,name='published-jobs'),
    path('published-jobs/delete-job/<slug:slug>/',views.delete_job,name='delete-job'),
    path('published-jobs/edit-job/<slug:slug>/', views.edit_job, name='edit-job'),
    path('published-jobs/<slug:slug>/applicants',views.get_applicants,name='get-applicants'),
    path('published-jobs/<slug:slug_job>/applicants/<slug:slug_resume>',views.resume_view,name='resume-view'),
    path('published-jobs/<slug:slug>/job-filled',views.job_filled,name='job-filled'),
    path('jobs/respond/<slug:slug>/',views.add_respond, name='respond'),
]