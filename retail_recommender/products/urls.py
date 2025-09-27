# products/urls.py
# products/urls.py
from django.urls import path
from . import views

# products/urls.py
urlpatterns = [
    path('', views.home, name='home'),  # Home URL
    path('search/', views.search_products, name='search_products'),
]
