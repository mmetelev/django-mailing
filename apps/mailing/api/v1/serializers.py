from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer
from timezone_field.rest_framework import TimeZoneSerializerField

from apps.mailing.models import MailingList, Message, Client, OperatorCode


class MailingListSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Рассылка"""
    tags = TagListSerializerField()

    class Meta:
        model = MailingList
        fields = ['id', 'start_dt', 'text', 'operator_code', 'tags', 'end_dt']


class MessageSerializer(serializers.ModelSerializer):
    """Сообщение"""

    class Meta:
        model = Message
        fields = ['id', 'create_dt', 'mailing_list', 'client']


class ClientSerializer(TaggitSerializer, serializers.ModelSerializer):
    """Клиент"""
    tags = TagListSerializerField()
    time_zone = TimeZoneSerializerField(use_pytz=False)
    operator_code = serializers.CharField()

    class Meta:
        model = Client
        fields = ['id', 'phone', 'operator_code', 'tags', 'time_zone']


class OperatorCodeSerializer(serializers.ModelSerializer):
    """Код оператора"""

    class Meta:
        model = OperatorCode
        fields = ['id', 'code']
