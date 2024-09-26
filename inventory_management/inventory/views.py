from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import InventoryItem
from .serializers import InventoryItemSerializer
from django.shortcuts import get_object_or_404
from django.core.cache import cache

class InventoryItemView(APIView):
    def get(self, request, item_id=None):
        item = cache.get(f'item_{item_id}')
        if not item:
            item = get_object_or_404(InventoryItem, id=item_id)
            cache.set(f'item_{item_id}', item)
        serializer = InventoryItemSerializer(item)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, item_id=None):
        item = get_object_or_404(InventoryItem, id=item_id)
        serializer = InventoryItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, item_id=None):
        item = get_object_or_404(InventoryItem, id=item_id)
        item.delete()
        return Response({"message": "Item deleted"}, status=status.HTTP_204_NO_CONTENT)