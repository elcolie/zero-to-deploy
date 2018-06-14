from django.contrib.auth.models import User
from django.db import models

from commons.models import AbstractTimestamp


class Order(AbstractTimestamp):
    """Assume product has no customization. If it has JSONField() is needed"""
    # GDPR: User has right to erase
    customer = models.ForeignKey(User, related_name='orders', related_query_name='orders', on_delete=models.SET_NULL,
                                 null=True)

    def __str__(self):
        return f"{self.customer}"
