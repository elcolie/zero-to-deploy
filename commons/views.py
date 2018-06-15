import logging

import django_rq
from django.contrib.auth.models import User
from push_notifications.models import GCMDevice
from rest_framework import views, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from commons.serializers import PushNotificationSerializer, worker_wrapper
from invoices.api.viewsets import IsStaffPermission

logger = logging.getLogger('django')


class PushContext:
    def __init__(self, user: User):
        self.user = user


class PushNotificationAPIView(views.APIView):
    """
    Staff posts to Notifies to his Customer Devices(SNT2DCS)
    """
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsStaffPermission)

    def post(self, request):
        # Since it is primitive APIView. I have to make my own context
        context = {
            'request': PushContext(request.user)
        }
        serializer = PushNotificationSerializer(data=request.data, context=context)
        if serializer.is_valid():
            """Enqueue job to rqworker and let it send the message with FCM"""
            devices = GCMDevice.objects.filter(user=serializer.validated_data.get('customer'))
            django_rq.enqueue(worker_wrapper, devices,
                              message=serializer.validated_data.get('message', ""),
                              extra=serializer.validated_data.get('extra', {'message': 'Blank'}))
            logger.info(f"data: {serializer.data}")
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
