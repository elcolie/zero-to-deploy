from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from commons.models import AbstractTimestamp


class Menu(AbstractTimestamp):
    class BackType(DjangoChoices):
        food = ChoiceItem(f"Food")
        drink = ChoiceItem(f"Drink")

    menu_type = models.CharField(max_length=15, choices=BackType.choices, default=BackType.food)
    name = models.CharField(max_length=20)
    image = models.ImageField(default='sr.png', upload_to='menus')
    take_home = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.price}"
