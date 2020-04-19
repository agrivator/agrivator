from django.urls import path,include
from . import views
from rest_framework import routers


router=routers.DefaultRouter()
router.register(r'user', views.UserViewset)
router.register(r'farmer', views.FarmerViewset)
router.register(r'shop', views.ShopViewset)
router.register(r'customer', views.CustomerViewset)
router.register(r'product', views.ProductViewset)

urlpatterns = router.urls
