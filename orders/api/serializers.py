from rest_framework import serializers

from menus.models import Menu
from order_items.api.serializers import ShortItemSerializer
from order_items.models import OrderItem
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:order-detail')
    customer = serializers.CurrentUserDefault()
    order_items = ShortItemSerializer(read_only=True, many=True)
    menus = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all(), many=True, write_only=True)

    class Meta:
        model = Order
        fields = [
            'url',
            'customer',
            'order_items',
            'menus',
            'sum',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        menus = validated_data.pop('menus')
        order = Order.objects.create(customer=validated_data.get('customer'))
        for item in menus:
            OrderItem.objects.bulk_create([
                OrderItem(order=order, menu=item)
            ])
        return order
