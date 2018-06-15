from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, BasePermission

from invoices.api.serializers import InvoiceSerializer
from invoices.models import Invoice


class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class InvoiceFilter(filters.FilterSet):
    customer_username = filters.CharFilter(name='order__customer__username', lookup_expr='icontains')
    customer_first_name = filters.CharFilter(name='order__customer__first_name', lookup_expr='icontains')
    created_at = filters.DateTimeFilter(name='created_at', lookup_expr='gte')
    updated_at = filters.DateTimeFilter(name='updated_at', lookup_expr='gte')

    class Meta:
        model = Invoice
        fields = [
            'customer_username',
            'customer_first_name',
            'created_at',
            'updated_at',
        ]


class InvoiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsStaffPermission)
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = InvoiceFilter
    search_fields = (
        'order__customer__username',
        'order__customer__first_name',
        'order__customer__last_name',
    )
