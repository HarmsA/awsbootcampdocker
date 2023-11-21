from django.contrib import admin
from django.urls import path, include
from . import views
    
urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<str:topic>', views.topic, name='topic'),
    path('qna', views.qna, name='qna'),
    path('search_tag', views.search_tag, name='search_tag'),
]
