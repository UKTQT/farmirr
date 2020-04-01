from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('', views.gsmara, name='gsmara'),
    path('gsmekle/', views.gsmekle,name='gsmekle'),
    path('cihazekle/',views.cihazekle,name='cihazekle'),
]