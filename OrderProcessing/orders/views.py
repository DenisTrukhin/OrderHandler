from rest_framework.viewsets import ModelViewSet
from orders.serializers import OrderSerializer
from orders.models import Order

# Create your views here.
class OrderViewSet(ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer