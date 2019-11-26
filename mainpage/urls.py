from django.conf.urls import url
from .views import ProjectListAndFormView
from django.urls import  include,path
urlpatterns = [
    path('',ProjectListAndFormView.as_view(),name='main')
]
