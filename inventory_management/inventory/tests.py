from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import InventoryItem

class InventoryItemTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.item = InventoryItem.objects.create(name="Test Item", description="A test item", quantity=10)

    def test_get_item(self):
        response = self.client.get(f'/items/{self.item.id}/')
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        data = {"name": "New Item", "description": "A new item", "quantity": 5}
        response = self.client.post('/items/', data)
        self.assertEqual(response.status_code, 201)

    def test_update_item(self):
        data = {"quantity": 15}
        response = self.client.put(f'/items/{self.item.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_delete_item(self):
        response = self.client.delete(f'/items/{self.item.id}/')
        self.assertEqual(response.status_code, 204)