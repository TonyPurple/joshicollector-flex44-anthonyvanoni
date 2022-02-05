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
  # associate an item with a Joshi (M:M)
  path('joshis/<int:joshi_id>/assoc_item/<int:item_id>/', views.assoc_item, name='assoc_item'),
  # unassociate an item and Joshi
  path('joshis/<int:joshi_id>/unassoc_item/<int:item_id>/', views.unassoc_item, name='unassoc_item'),
  path('items/', views.ItemList.as_view(), name='items_index'),
  path('items/<int:pk>/', views.ItemDetail.as_view(), name='items_detail'),
  path('items/create/', views.ItemCreate.as_view(), name='items_create'),
  path('items/<int:pk>/update/', views.ItemUpdate.as_view(), name='items_update'),
  path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='items_delete'),
]