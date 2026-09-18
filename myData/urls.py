from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("stream/add/", views.add_stream, name="add_stream"),
    path("stream/data/", views.get_streams, name="get_streams"),
]