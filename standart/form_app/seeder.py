from .models import Application, Requisites
import random


type_paid = ['карта', 'платёжный счёт']
type_card_payment_account = ['тип1', 'тип2']
surname = ['Васёв', 'Вахрамеев', 'Петров', 'Васильев', 'Иванов', 'Сидоров', 'Козлов', 'Баранов', 'Ослов', 'Мудозвонов',
           'Перепёлкин', 'Глухаркин', 'Собакевич', 'Котов', 'Мышкин']
name = ['Олег', 'Антон', 'Дмитрий', 'Сергей', 'Андрей', 'Николай', 'Василий', 'Семён', 'Пётр', 'Алексей', 'Геннадий',
        'Александр', 'Акинфий', 'Виктор']
patronymic = ['Олегович', 'Антонович', 'Дмитриевич', 'Сергеевич', 'Андреевич', 'Николаевич', 'Васильевич', 'Семёнович',
              'Петрович', 'Алексеевич', 'Геннадьевич', 'Александрович', 'Акинфиевич', 'Викторович']
status = ['Ожидает оплаты', 'Оплачена', 'Отменена']


def my_seed():
    count_requisites = 0
    count_application = 0
    while count_requisites < 101:
        r_type_paid = random.choice(type_paid)
        r_type_card_payment_account = random.choice(type_card_payment_account)
        r_surname = random.choice(surname)
        r_name = random.choice(name)
        r_patronymic = random.choice(patronymic)
        r_phone_number = random.randint(89000000000, 89999999999)
        r_limit = random.randint(1000, 100000)

        Requisites.objects.create(
            type_paid=r_type_paid,
            type_card_payment_account=r_type_card_payment_account,
            surname=r_surname,
            name=r_name,
            patronymic=r_patronymic,
            phone_number=r_phone_number,
            limit=r_limit
        )

        count_requisites += 1

    requisites = Requisites.objects.all()

    while count_application < 5001:
        r_requisites = random.choice(requisites)
        r_status = random.choice(status)
        r_summ = random.randint(1000, 100000)
        Application.objects.create(
            summ=r_summ,
            requisites=r_requisites,
            status=r_status
        )

        count_application +=1

