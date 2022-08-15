from django.db import models

from taggit.managers import TaggableManager
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField


class OperatorCode(models.Model):
    """Код оператора"""
    code = models.CharField('код мобильного оператора', max_length=3)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'код оператора'
        verbose_name_plural = 'коды операторов'


class MailingList(models.Model):
    """Рассылка"""
    start_dt = models.DateTimeField('дата и время запуска рассылки')
    text = models.TextField('текст сообщения', max_length=500)
    operator_code = models.ForeignKey(
        OperatorCode,
        related_name='+',
        on_delete=models.CASCADE,
        verbose_name='код мобильного оператора',
    )
    tags = TaggableManager(blank=True)
    end_dt = models.DateTimeField('дата и время окончания рассылки')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'рассылку'
        verbose_name_plural = 'рассылки'


class Client(models.Model):
    """Клиент"""
    phone = PhoneNumberField('номер телефона', null=False, blank=False, unique=True)
    operator_code = models.ForeignKey(
        OperatorCode,
        verbose_name='код мобильного оператора',
        related_name='+',
        on_delete=models.CASCADE
    )
    tags = TaggableManager()
    time_zone = TimeZoneField(
        'часовой пояс',
        default='Europe/Moscow',
        choices_display="WITH_GMT_OFFSET"
    )

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'клиента'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    """Сообщение"""
    create_dt = models.DateTimeField('дата и время создания', auto_now_add=True)
    mailing_list = models.OneToOneField(
        MailingList,
        verbose_name='рассылка',
        on_delete=models.CASCADE,
    )
    client = models.ManyToManyField(
        Client,
        verbose_name='клиент'
    )

    def __str__(self):
        return str(self.mailing_list.text)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
