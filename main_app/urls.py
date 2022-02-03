from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('joshis/', views.joshis_index, name='index'),
  path('joshis/<int:joshi_id>/', views.joshis_detail, name='detail'),
]