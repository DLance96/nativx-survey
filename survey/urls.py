from django.conf.urls import url
from . import views

app_name = 'survey'

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^finished/$', views.home, name="finished"),

]
