from rest_framework.viewsets import ModelViewSet
from mainapp.models import Cart,Product,CartProduct
from mainapp.serializer import CartProductSerializer, CartSerializer, ProductSerializer



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartProductViewSet(ModelViewSet):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

