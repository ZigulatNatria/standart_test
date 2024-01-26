from django.urls import path
from .views import ApplicationsView, RequisitesView, search, sort, start_seed


urlpatterns = [
    path('', ApplicationsView.as_view(), name='application'),
    path('requisites/', RequisitesView.as_view(), name='requisites'),
    path('search/', search, name='search'),
    path('sort/', sort, name='sort'),
    path('start_seed/', start_seed, name='start_seed')
]