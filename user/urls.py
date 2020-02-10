"""
    user/urls.py

    This Url module is from the User app.
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
]
