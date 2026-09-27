from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path("stream/add/", views.add_stream, name="add_stream"),
    path("stream/data/", views.get_streams, name="get_streams"),
    path("stream/update/<int:id>/", views.update_stream, name="update_stream"),
    path("stream/delete/<int:id>/", views.delete_stream, name="delete_stream"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)