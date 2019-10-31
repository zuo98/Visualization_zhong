from django.urls import path
from vis_app import views


urlpatterns = [
    path('', views.getHome, name='home'),
    # path('map', views.getHighCountMap, name='map'),
    path('yearmap', views.getHighYearCountMap, name='yearmap'),
    path('airtem', views.airtemMapTimeline, name='airtem')
]
