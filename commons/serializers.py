import typing

from django.contrib.auth.models import User
from push_notifications.models import GCMDeviceQuerySet
from rest_framework import serializers


def worker_wrapper(devices: GCMDeviceQuerySet, message: str = "", extra: typing.Dict[str, str] = None):
    """
    Wrapper for Firebase
    :param devices:
    :param message:
    :param extra:
    :return:
    """
    devices.send_message(message, extra=extra)


class PushNotificationSerializer(serializers.Serializer):
    extra = serializers.JSONField()
    message = serializers.CharField(max_length=255, required=False)
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    staff = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        customer = attrs.get('customer')
        staff = attrs.get('staff')
        if customer.userprofile.selected_company != staff.userprofile.selected_company:
            data = {
                'customer_selected_company': f"{customer} does not belong to {staff.userprofile.selected_company}"
            }
            raise serializers.ValidationError(detail=data)
        return attrs
