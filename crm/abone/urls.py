from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('aboneekle/',views.aboneEkle, name='aboneekle'),
    path('aboneara/',views.aboneAra,name='aboneara')

]