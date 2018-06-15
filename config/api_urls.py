from rest_framework import routers

from invoices.api.viewsets import InvoiceViewSet
from menus.api.viewsets import MenuViewSet
from order_items.api.viewsets import OrderItemViewSet
from orders.api.viewsets import OrderViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, base_name='order')
router.register(r'order-items', OrderItemViewSet, base_name='order_item')
router.register(r'invoices', InvoiceViewSet, base_name='invoice')
router.register(r'menus', MenuViewSet, base_name='menu')

urlpatterns = router.urls
