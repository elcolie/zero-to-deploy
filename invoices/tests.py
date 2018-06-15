from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from commons.tests import make_food, make_order
from invoices.models import Invoice
from orders.models import Order
from orders.tests import AdminClientMixin


class TestInvoice(AdminClientMixin, TestCase):
    def setUp(self):
        super().setUp()

    def test_related_name(self):
        make_food()
        make_order(self.admin)
        order = Order.objects.first()
        Invoice.objects.create(order=order, cashier=self.admin)
        order.refresh_from_db()
        assert isinstance(order.invoice, Invoice)

    def test_related_query_name(self):
        mommy.make(Invoice, _quantity=10, cashier=self.admin)
        invoice = Invoice.objects.first()
        user = User.objects.filter(invoices=invoice).first()
        assert self.admin == user

    def test_staff(self):
        customer = User.objects.create(username='Bach', email='bach@example.com', password='tewiojkl;dfa')
        client = APIClient()
        client.force_authenticate(user=customer)
        url = reverse('api:invoice-list')
        res = client.get(url)
        msg = f"You do not have permission to perform this action."
        assert status.HTTP_403_FORBIDDEN == res.status_code
        assert msg == str(res.data.get('detail'))