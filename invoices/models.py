from django.contrib.auth.models import User
from django.db import models

from commons.models import AbstractTimestamp
from orders.models import Order


class Invoice(AbstractTimestamp):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='invoice', related_query_name='invoice')
    cashier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices', related_query_name='invoices')

    def __str__(self):
        return f"{self.order}"
