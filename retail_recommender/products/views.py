# products/views.py
from django.shortcuts import render
from .models import Product
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

def search_products(request):
    query = request.GET.get('q')
    if query:
        results = Product.objects.filter(
            Q(description__icontains=query) | Q(stock_code__icontains=query)
        )
    else:
        results = Product.objects.all()

    return render(request, 'search_results.html', {'results': results, 'query': query})
