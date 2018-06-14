from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy

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
