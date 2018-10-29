from django.conf.urls import url

from search import views

urlpatterns = [
    url(r'^searchform/$', views.search_form),
    url(r'^search/$', views.search, name='search'),
    url(r'^suggest/$', views.suggest, name='suggest'),
]