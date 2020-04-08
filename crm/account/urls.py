from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view,name='accountLogin'),
    path('home/', views.home,name='home'),
    path('logout/', views.logout_view,name='logout'),
]