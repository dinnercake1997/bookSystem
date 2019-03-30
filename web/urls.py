from django.conf.urls import url
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    url(r'^favorites', views.favorites),
    url(r'^login', views.login),
    # url(r'^welcome',views.welcome ),
    url(r'^register', views.register),
    url(r'^home', views.home),
    url(r'^PCenter', views.PCenter),
    url(r'^upload',views.upload),
    url(r'^selling',views.selling),
    url(r'^book/$', views.book),
    url(r'^book_col/$', views.book_col),
    url(r'^book_cal/$', views.book_cal),
    url(r'^own_book/$', views.own_book),
    url(r'^book_result', views.book_result),
    url(r'^buyer_center/$', views.buyer_center),
    url(r'^seller_center', views.seller_center),
    url(r'^comment/$', views.comment),
    url(r'^tobuyer_comment/$', views.tobuyer_comment),
    url(r'^others_center/$', views.others_center),
    url(r'^favorites', views.favorites),
    url(r'^success_return/$', views.success_return),
]

urlpatterns += staticfiles_urlpatterns()