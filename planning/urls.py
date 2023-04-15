from django.urls import path
from .views import *

urlpatterns = [
    path('interview_planning/', InterviewPlanning.as_view(), name='interview-planning'),
    path('interview_planning/interview/<int:pk>', InterviewDetail.as_view(), name='interview-detail'),
    path('interview_planning/interview-create', InterviewCreate.as_view(), name='interview-create'),
    path('interview_planning/interview-delete/<int:pk>', InterviewDelete.as_view(), name='interview-delete'),
    path('interview_planning/interview-edit/<int:pk>', InterviewEdit.as_view(), name='interview-edit'),
]