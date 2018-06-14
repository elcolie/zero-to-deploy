from rest_framework import viewsets

from order_items.api.serializers import OrderItemSerializer
from order_items.models import OrderItem


class OrderItemViewSet(viewsets.ModelViewSet):
    """Provide this endpoint in case customer would like to change the menu in his order"""
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
