from django.urls import path
from list import views as list_views

urlpatterns = [
    path("", list_views.list),
]
