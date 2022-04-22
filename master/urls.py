from django.urls import path
from master import views

urlpatterns = [
     path('', views.index, name='index'),
     path('exit/', views.exit, name="exit"),
]