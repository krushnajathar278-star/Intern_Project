# products/models.py
from django.db import models

class Product(models.Model):
    stock_code = models.CharField(max_length=20)
    description = models.TextField()
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    invoice_date = models.DateTimeField()
    customer_id = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.description
