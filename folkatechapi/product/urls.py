from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('list-product/', ProductListView.as_view(), name='list-product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
