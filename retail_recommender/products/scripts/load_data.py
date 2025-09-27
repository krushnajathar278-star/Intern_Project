# products/scripts/load_data.py
import pandas as pd
from products.models import Product
from django.utils.dateparse import parse_datetime

def load_data(file_path):
    data = pd.read_excel(file_path)
    for index, row in data.iterrows():
        Product.objects.create(
            stock_code=row['StockCode'],
            description=row['Description'],
            quantity=row['Quantity'],
            unit_price=row['UnitPrice'],
            invoice_date=parse_datetime(str(row['InvoiceDate'])),
            customer_id=row['CustomerID'] if pd.notnull(row['CustomerID']) else None
        )

