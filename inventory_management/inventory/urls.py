from django.urls import path
from .views import InventoryItemView  # Import InventoryItemView from views.py

urlpatterns = [
    path('items/', InventoryItemView.as_view(), name='create_item'),
    path('items/<int:item_id>/', InventoryItemView.as_view(), name='item_detail'),
]