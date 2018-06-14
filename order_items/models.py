from django.db import models

from commons.models import AbstractTimestamp
from menus.models import Menu
from orders.models import Order


class OrderItem(AbstractTimestamp):
    order = models.ForeignKey(Order, related_name='order_items', related_query_name='order_items',
                              on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, related_name='menus', related_query_name='menus', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.menu}"
