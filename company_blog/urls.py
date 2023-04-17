from django.urls import path
from .views import *

urlpatterns = [
    path('company-blog/<slug:slug>/', PostView.as_view() , name='company-blog-list'),
    path('company-blog/<slug:slug_company>/<slug:slug_post>', PostDetail.as_view() , name='company-blog-detail'),
    path('company-blog/<slug:slug_company>/<slug:slug>/post-delete', post_delete , name='post-delete'),
    path('company-blog/<slug:slug_company>/<slug:slug>/post-edit', post_edit, name='post-edit'),
    path('company-blog/<slug:slug_company>/<slug:slug_post>/add-comment', add_comment, name='add-comment'),
    path('company-blog/<slug:slug_company>/<slug:slug_post>/add-reply-comment', add_reply_comment, name='add-reply-comment'),
    path('company-blogs/', company_blogs, name='company-blogs'),
    path('company-blogs/create-post', create_post, name='create-post'),
]