from django.urls import path
from . import views

app_name = "logs"

urlpatterns = [
    path("", views.calendar, name="calendar"),
    path("get-logs/", views.get_logs, name="get_logs"),
    path("write/", views.write, name="write"),
    path("<int:log_id>/", views.detail, name="detail"),
]
