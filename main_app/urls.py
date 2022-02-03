from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('joshis/', views.joshis_index, name='index'),
  path('joshis/<int:joshi_id>/', views.joshis_detail, name='detail'),
  path('joshis/create/', views.JoshiCreate.as_view(), name='joshis_create'),
  path('joshis/<int:pk>/update/', views.JoshiUpdate.as_view(), name='joshis_update'),
  path('joshis/<int:pk>/delete/', views.JoshiDelete.as_view(), name='joshis_delete'),
]