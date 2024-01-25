from django.db import models


class Requisites(models.Model):
    TYPE_PAID_CHOICES = [
        ('card', 'карта'),
        ('payment_account', 'платёжный счёт'),
    ]

    TYPE_CARD_ACCOUNT_CHOICES = [
        ('type1', 'тип1'),
        ('type2', 'тип2'),
    ]

    type_paid = models.CharField(
        verbose_name='тип платежа',
        choices=TYPE_PAID_CHOICES,
        max_length=15,
        default='card'
    )
    type_card_payment_account = models.CharField(
        verbose_name='тип карты/счета',
        choices=TYPE_CARD_ACCOUNT_CHOICES,
        max_length=5,
        default='type1'
    )
    surname = models.CharField(verbose_name='фамилия', max_length=128)
    name = models.CharField(verbose_name='имя', max_length=128)
    patronymic = models.CharField(verbose_name='отчество', max_length=128, null=True, blank=True)
    phone_number = models.BigIntegerField(verbose_name='номер телефона')
    limit = models.IntegerField(verbose_name='лимит', default=10000)

    class Meta:
        verbose_name = 'реквизит'
        verbose_name_plural = 'реквизиты'

    def __str__(self):
        return '{}'.format(self.surname) + ' ' + '{}'.format(self.name) + ' ' + '{}'.format(self.patronymic)


class Application(models.Model):
    STATUS_CHOICES = [
        ('awaiting_payment', 'Ожидает оплаты'),
        ('paid', 'Оплачена'),
        ('canceled', 'Отменена'),
    ]

    summ = models.DecimalField(verbose_name='сумма', max_digits=10, decimal_places=2)
    requisites = models.ForeignKey(Requisites, verbose_name='реквизиты', on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name='статус',
        choices=STATUS_CHOICES,
        max_length=16,
        default='awaiting_payment'
    )

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return '{}'.format(self.id) + ' ' + '{}'.format(self.requisites)