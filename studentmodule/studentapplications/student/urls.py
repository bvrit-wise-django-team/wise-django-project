from django.conf.urls import url
from student import views
from django.contrib import admin

urlpatterns=[url(r'^$',views.index,name='home'),]

