from django.db import models


class Requisites(models.Model):
    TYPE_PAID_CHOICES = [
        ('карта', 'карта'),
        ('платёжный счёт', 'платёжный счёт'),
    ]

    TYPE_CARD_ACCOUNT_CHOICES = [
        ('тип1', 'тип1'),
        ('тип2', 'тип2'),
    ]

    type_paid = models.CharField(
        verbose_name='тип платежа',
        choices=TYPE_PAID_CHOICES,
        max_length=15,
        # default='card'     #Seeder при дефолтном значении всегда ставит его (((((
    )
    type_card_payment_account = models.CharField(
        verbose_name='тип карты/счета',
        choices=TYPE_CARD_ACCOUNT_CHOICES,
        max_length=5,
        # default='type1'    #Seeder при дефолтном значении всегда ставит его (((((
    )
    surname = models.CharField(verbose_name='фамилия', max_length=10)
    name = models.CharField(verbose_name='имя', max_length=10)
    patronymic = models.CharField(verbose_name='отчество', max_length=10, null=True, blank=True)
    phone_number = models.BigIntegerField(verbose_name='номер телефона')
    limit = models.IntegerField(verbose_name='лимит')

    class Meta:
        verbose_name = 'реквизит'
        verbose_name_plural = 'реквизиты'

    def __str__(self):
        return '{}'.format(self.surname) + ' ' + '{}'.format(self.name) + ' ' + '{}'.format(self.patronymic)


class Application(models.Model):
    STATUS_CHOICES = [
        ('Ожидает оплаты', 'Ожидает оплаты'),
        ('Оплачена', 'Оплачена'),
        ('Отменена', 'Отменена'),
    ]

    # summ = models.DecimalField(verbose_name='сумма', max_digits=10, decimal_places=2)
    summ = models.IntegerField(verbose_name='сумма')   # для суммы DecimalField больше подходит, но Seeder не корректно с ним работает
    requisites = models.ForeignKey(Requisites, verbose_name='реквизиты', on_delete=models.CASCADE)
    status = models.CharField(
        verbose_name='статус',
        choices=STATUS_CHOICES,
        max_length=16,
        default='awaiting_payment'  #Seeder при дефолтном значении всегда ставит его (((((
    )

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return '{}'.format(self.id) + ' ' + '{}'.format(self.requisites)
