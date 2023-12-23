
from django.urls import path,include
# from .views import APIProductList,APIProduct,APICategoryList,APICategory
from . import views

# DRF 
from rest_framework.routers import DefaultRouter




#Routers 
router = DefaultRouter()
router.register("products",views.ProductViewSet)
router.register("categories",views.CategoryViewSet) 
urlpatterns = router.urls
 



urlpatterns = [

    path("",include(router.urls))
    # path("products/",APIProductList.as_view(),name='api-products-list'),
    # path("products/<str:pk>/",APIProduct.as_view(),name='api-product'),

    # path("categories/",APICategoryList.as_view(),name='api-categories-list'),
    # path("categories/<str:pk>/",APICategory.as_view(),name='api-category'),

]

