from django.urls import path
from . import views
urlpatterns = [
    path('', views.single_website_view, name='website_view'),
    path('/multiple', views.multiple_website_view, name='get_multiple_websites')
]
