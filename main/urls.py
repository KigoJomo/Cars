from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("local/", views.local, name="local"),
    path("imports/", views.imports, name="imports"),
    path("car/<int:carId>", views.details, name="car"),
    path("search/", views.search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

