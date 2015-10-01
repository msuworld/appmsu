from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.graph, name='graph'),
    url(r'^api/play_count_by_month$', views.play_count_by_month, name='play_count_by_month'),
     url(r'^sentiment$', views.sentiment, name='sentiment'),
     url(r'^users$', views.users, name='users'),
     url(r'^search$', views.search, name='search'),
     url(r'^tiframe$', views.tiframe, name='tiframe'),   
    
]