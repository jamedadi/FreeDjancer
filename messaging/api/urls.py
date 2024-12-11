from django.urls import path
from . import views

urlpatterns = [
    path('chats/', views.ChatList.as_view(), name='chat-list'),
    path('chats/<int:chat_id>/messages/', views.MessageList.as_view(),
         name='message-list'),
]
