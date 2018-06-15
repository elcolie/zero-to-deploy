from rest_framework import serializers

from invoices.models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:invoice-detail')
    order_url = serializers.HyperlinkedRelatedField(view_name='api:order-detail', source='order', read_only=True)
    cashier = serializers.CurrentUserDefault()

    class Meta:
        model = Invoice
        fields = [
            'url',
            'order_url',
            'order',
            'cashier',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
