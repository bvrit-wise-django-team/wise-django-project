from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^name/$', views.name),
        url(r'^get_name/$', views.get_name, name = "myurl"),
        url(r'^viewNames/$', views.viewNames, name = "view_names"),
]
