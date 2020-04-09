from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('cihazekle/',views.cihazekle,name='cihazekle'),
    path('stokdetay/',views.stokDetay,name='stokdetay'),
    path('stoksatis/',views.stoksatisyonlendirme,name='stoksatis'),
    path('stokcikis/',views.stokcikis,name='stokcikis'),
]