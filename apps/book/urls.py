from django.conf.urls import url
from. import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.books),
    url(r'^remove/(?P<id>\d+)$', views.remove),
]
