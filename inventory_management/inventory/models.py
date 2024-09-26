from django.db import models

# Create your models here.

class InventoryItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self):
        return self.name