from django.urls import path
from . import views
urlpatterns = [
    path('', views.prediction, name="predictions"),
    path('results/', views.results, name="results"),
    path('summary/', views.summary, name="summary"),
]