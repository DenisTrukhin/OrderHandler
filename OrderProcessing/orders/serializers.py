from rest_framework import serializers
from orders.models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Order
		fields = ('id', 'description', 'price')