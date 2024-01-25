from django.urls import path
from .views import ApplicationsView, RequisitesView, search


urlpatterns = [
    path('', ApplicationsView.as_view(), name='application'),
    path('requisites/', RequisitesView.as_view(), name='requisites'),
    path('search/', search, name='search')
]