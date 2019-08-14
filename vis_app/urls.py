from django.urls import path
from vis_app import views


urlpatterns = [
    path('', views.getHome, name='home'),
    path('map', views.getHighCountMap, name='map'),
]
