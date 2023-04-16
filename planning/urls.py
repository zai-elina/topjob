from django.urls import path
from .views import *

urlpatterns = [
    path('interview-planning/', InterviewPlanning.as_view(), name='interview-planning'),
    path('interview-planning/interview/<int:pk>', InterviewDetail.as_view(), name='interview-detail'),
    path('interview-planning/interview-create', InterviewCreate.as_view(), name='interview-create'),
    path('interview-planning/interview-delete/<int:pk>', InterviewDelete.as_view(), name='interview-delete'),
    path('interview-planning/interview-edit/<int:pk>', InterviewEdit.as_view(), name='interview-edit'),
]