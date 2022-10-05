from rest_framework.routers import DefaultRouter as DR

from mainapp.views import(
    ProductViewSet,CartViewSet, CartProductViewSet
)

router = DR()

router.register('product',ProductViewSet,basename = 'product')

router.register('cart',CartViewSet,basename = 'cart')

router.register('cartproduct',CartProductViewSet, basename='cartproduct')

urlpatterns = []

urlpatterns += router.urls