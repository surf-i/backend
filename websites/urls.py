from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.multiple_website_view, name="websites_view"),
    path('get/<str:pk>', views.single_website_view, name='website_view'),
]
