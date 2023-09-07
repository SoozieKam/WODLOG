from django.urls import path
from . import views

app_name = "logs"

urlpatterns = [
    path("", views.calendar, name="calendar"),
    path("write/<str:selected_date>/", views.write, name="write"),
]
