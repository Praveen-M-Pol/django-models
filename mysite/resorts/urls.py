from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^(?P<resort_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<resort_id>[0-9]+)/results$', views.results, name="results"),
    url(r'^(?P<resort_id>[0-9]+)/dish$', views.dish, name="dish"),
    url(r'^(?P<resort_id>[0-9]+)/resortReview', views.resortReview, name="resortReview"),
]