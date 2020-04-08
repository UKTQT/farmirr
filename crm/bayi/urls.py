from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('bayiekle/',views.bayiEkle, name='bayiekle'),
    path('bayidetay/',views.bayiDetay,name='bayidetay')
]