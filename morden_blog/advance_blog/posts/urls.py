from django.urls import path
from posts.views import post_create, post_delete, post_list, post_update, post_detail

app_name= 'post'

urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create, name='create'),
    path('<str:slug>/update/', post_update, name='update'),
    path('<str:slug>/delete/', post_delete, name='delete'),
    path('<str:slug>/', post_detail, name='detail'),
]
