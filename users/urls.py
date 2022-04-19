from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_review_view, name="add_review_view")
]