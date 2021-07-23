from django.contrib import admin
from django.urls import path

from . import views

app_name = "entry"

urlpatterns = [
    path(r'', views.EntryView.as_view(), name="entries"),
    path(r'create/', views.CreateEntryView.as_view(), name="create"),
]
