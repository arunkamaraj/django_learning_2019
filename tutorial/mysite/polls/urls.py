from django.urls import include, path
from . import views

app_name ='polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailPageView.as_view(), name='detail'),
    path('<int:quest_id>/result/', views.result, name='result'),
    path('<int:quest_id>/vote/', views.vote, name='vote'),
    path('upload/', views.upload_file, name='upload'),
    path('book/', views.book_list, name='booklist'),
    path('book/bookupload/', views.book_upload, name='bookupload'),
    path('<int:pk>/deletebook/', views.book_delete, name='delete')
]