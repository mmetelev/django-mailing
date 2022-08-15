from rest_framework.viewsets import ModelViewSet

from apps.mailing.models import Client, MailingList, Message, OperatorCode
from .serializers import ClientSerializer, MailingListSerializer, \
    MessageSerializer, OperatorCodeSerializer


class ClientViewSet(ModelViewSet):
    """Клиент"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingListViewSet(ModelViewSet):
    """Рассылка"""
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer


class OperatorCodeViewSet(ModelViewSet):
    """Код оператора"""
    queryset = OperatorCode.objects.all()
    serializer_class = OperatorCodeSerializer


class MessageViewSet(ModelViewSet):
    """Сообщение"""
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
