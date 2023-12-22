
from django.urls import path
from .views import APIProductList,APIProduct,APICategoryList,APICategory

urlpatterns = [
    path("products/",APIProductList.as_view(),name='api-products-list'),
    path("products/<str:pk>/",APIProduct.as_view(),name='api-product'),

    path("categories/",APICategoryList.as_view(),name='api-categories-list'),
    path("categories/<str:pk>/",APICategory.as_view(),name='api-category'),



]
