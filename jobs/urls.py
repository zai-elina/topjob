from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('jobs/', views.job_list, name='job-list'),
    path('jobs/company-jobs/<slug:slug>', views.company_jobs, name='company-jobs'),
    path('jobs/<slug:slug>/', views.JobDetailView.as_view(), name='job-detail'),
    path('category-list/',views.category_list,name='category-list'),
    path('category-list/<slug:slug>/',views.category_detail,name='category-detail'),
    path('create-company/',views.create_company,name='create-company'),
    path('create-job/',views.create_job,name='create-job'),
    path('published-jobs/',views.published_jobs,name='published-jobs'),
    path('published-jobs/delete-job/<slug:slug>/',views.delete_job,name='delete-job'),
    path('published-jobs/edit-job/<slug:slug>/', views.edit_job, name='edit-job'),
    path('published-jobs/<slug:slug>/applicants',views.get_applicants,name='get-applicants'),
    path('resume-list/<slug:slug_resume>',views.ResumeDetailView.as_view(),name='resume-view'),
    path('published-jobs/<slug:slug>/applicants/delete-applicant/<int:apply_id>',views.delete_apply,name='delete-apply'),
    path('published-jobs/<slug:slug>/job-filled',views.job_filled,name='job-filled'),
    path('jobs/<slug:slug>/apply',views.send_cover_letter, name='send-cover-letter'),
]