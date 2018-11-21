from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('top', views.RatingView.as_view(), name='rating'),
]
