from django.urls import path
from wods import views

app_name = "wods"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:wod_id>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("<int:wod_id>/delete/", views.delete, name="delete"),
    path("<int:wod_id>/like/", views.likes, name="wod_like"),
    path("<int:wod_id>/bookmark/", views.bookmark, name="wod_bookmark"),
    path("search/", views.search, name="search"),
    path("search/name/", views.search_by_name, name="search_by_name"),
]
