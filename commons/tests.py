from decimal import Decimal

from model_mommy import mommy

from menus.models import Menu
from order_items.models import OrderItem
from orders.models import Order


def make_food():
    mommy.make(Menu, price=Decimal('221'), name='PadTai')
    mommy.make(Menu, price=Decimal('250'), name='KhaoPad')


def make_order(user):
    order = Order.objects.create(customer=user)
    OrderItem.objects.bulk_create([
        OrderItem(order=order, menu=Menu.objects.first()),
        OrderItem(order=order, menu=Menu.objects.last()),
    ])
    return order