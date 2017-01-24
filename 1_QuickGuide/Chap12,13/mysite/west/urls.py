from django.conf.urls import include, url
from west import views

urlpatterns = [
    url(r'^$', views.first_page),
    url(r'^staff', views.staff),
    url(r'^templay', views.templay),
    url(r'^form', views.form),
    url(r'^investigate', views.investigate),
    url(r'^login', views.user_login),
    url(r'^register', views.register),
]