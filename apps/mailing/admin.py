from django import forms
from django.contrib import admin

from .models import Message, MailingList, Client, OperatorCode
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class CountryForm(forms.ModelForm):
    """Форма для выбора региона"""

    class Meta:
        widgets = {
            'phone': PhoneNumberPrefixWidget(initial='RU'),
        }


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Сообщение"""
    pass


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    """Рассылка"""
    list_filter = ('operator_code',)
    search_fields = ('text',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Клиент"""
    list_filter = ('operator_code',)
    form = CountryForm


@admin.register(OperatorCode)
class OperatorCodeAdmin(admin.ModelAdmin):
    """Код мобильного оператора"""
    search_fields = ('operator_code',)
