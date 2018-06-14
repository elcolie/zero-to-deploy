from decimal import Decimal

from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from commons.tests import make_food, make_order
from commons.utils import MockRequest
from menus.models import Menu
from order_items.models import OrderItem
from orders.api.serializers import OrderSerializer
from orders.models import Order


class AdminClientMixin:
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', email='sarit@elcolie.com',
                                                   password='Queij5Chim8Rohne')
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin)


class TestOrderModel(AdminClientMixin, TestCase):

    def test_order_serializer(self):
        """Expect failed to make nested order/order-item"""
        customer_context = {
            'request': MockRequest(self.admin)  # sarit is a customer
        }
        data = {
            'menus': [1, 1, 2, 3]
        }
        serializer = OrderSerializer(data=data, context=customer_context)
        is_valid = serializer.is_valid()
        msg = 'Invalid pk "1" - object does not exist.'
        assert False is is_valid
        assert msg == str(serializer.errors.get('menus')[0])

    # Expect passed
    def test_nested_order(self):
        mommy.make(Menu, _quantity=2)
        data = {
            'menus': [
                Menu.objects.first().id,
                Menu.objects.last().id,
            ]
        }
        url = reverse('api:order-list')
        res = self.client.post(url, data=data, format='json')
        assert status.HTTP_201_CREATED == res.status_code
        assert 2 == OrderItem.objects.count()
        assert 1 == Order.objects.count()

    def test_sum_amount(self):
        make_food()
        order = make_order(self.admin)
        assert Decimal('471') == order.sum
