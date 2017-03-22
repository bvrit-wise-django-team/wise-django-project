from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^next/$', views.email, name='next'),
    url(r'^success/$', views.success, name='success'),
]
