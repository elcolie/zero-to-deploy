from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from menus.api.serializers import MenuSerializer
from menus.models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    __basic_fields = [
        'menu_type',
        'name',
        'take_home',
        'price',
    ]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

