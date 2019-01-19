from django.urls import path, include
from .views import *



urlpatterns = [
    path('', messages_list, name='test_html'),
    path('message/create/', MessageCreate.as_view(), name='message_create_url'),
    path('accounts', include('allauth.urls')),
    path('message/<str:slug>/', MessageDetail.as_view(), name='message_detail_url'),
    path('message/<str:slug>/update/', MessageUpdate.as_view(), name='message_update_url'),
    path('message/<str:slug>/user_answer/', MessageAnswer.as_view(), name='user_answer_url'),
    path('message/<str:slug>/delete/', MessageDelete.as_view(), name='message_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete', TagDelete.as_view(), name='tag_delete_url'),





]