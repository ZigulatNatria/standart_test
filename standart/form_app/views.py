from django.shortcuts import render
from django.views.generic import ListView
from .models import Application, Requisites
from django.db.models import Q
from .seeder import my_seed


class ApplicationsView(ListView):
    model = Application
    context_object_name = 'applications'
    template_name = 'applications.html'


class RequisitesView(ListView):
    model = Requisites
    context_object_name = 'requisites'
    template_name = 'requisites.html'


def search(request):
    search_query = request.GET.get('search', '') # передаётся имя ввода (строка поиска)

    if search_query:
        requisites = Requisites.objects.filter(
            Q(type_paid__icontains=search_query) | Q(type_paid__icontains=search_query.capitalize()) | Q(type_paid__icontains=search_query.casefold())
            | Q(type_card_payment_account__icontains=search_query) | Q(
                type_card_payment_account__icontains=search_query.capitalize()) | Q(type_card_payment_account__icontains=search_query.casefold())
            | Q(surname__icontains=search_query) | Q(surname__icontains=search_query.capitalize()) | Q(surname__icontains=search_query.casefold())
            | Q(name__icontains=search_query) | Q(name__icontains=search_query.capitalize()) | Q(name__icontains=search_query.casefold())
            | Q(patronymic__icontains=search_query) | Q(patronymic__icontains=search_query.capitalize()) | Q(patronymic__icontains=search_query.casefold())
            | Q(phone_number__icontains=search_query) | Q(phone_number__icontains=search_query.capitalize()) | Q(phone_number__icontains=search_query.casefold())
            | Q(limit__icontains=search_query) | Q(limit__icontains=search_query.capitalize()) | Q(limit__icontains=search_query.casefold())

        )
    else:
        requisites = Requisites.objects.all()
    context = {'requisites': requisites,}
    return render(request, 'search.html', context)


def sort(request):
    sort_query = request.GET.get('sort', '') # передаётся имя ввода (строка поиска)
    print(sort_query)

    if sort_query:
        requisites = Requisites.objects.order_by(sort_query)
    else:
        # requisites = Requisites.objects.all()
        requisites = None
    context = {'requisites': requisites,}
    return render(request, 'sort.html', context)


def start_seed(request):
    my_seed()
    return render(request, 'seed_response.html')

