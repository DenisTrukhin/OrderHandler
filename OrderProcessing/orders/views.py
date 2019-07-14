from rest_framework.viewsets import ModelViewSet
from orders.serializers import OrderSerializer
from orders.models import Order


class OrderViewSet(ModelViewSet):
	"""
	A ViewSet for viewing and editing orders.
	"""
	queryset = Order.objects.all()
	serializer_class = OrderSerializer