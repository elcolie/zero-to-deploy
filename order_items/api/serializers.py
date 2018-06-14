from rest_framework import serializers

from order_items.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'order',
            'menu',
        ]


class ShortItemSerializer(serializers.ModelSerializer):
    menu_url = serializers.HyperlinkedRelatedField(read_only=True, view_name='api:menu-detail', source='menu')
    menu_name = serializers.CharField(source='menu.name')

    class Meta:
        model = OrderItem
        fields = [
            'menu_url',
            'menu_name',
        ]
