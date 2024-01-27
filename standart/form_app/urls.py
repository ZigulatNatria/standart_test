from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import ApplicationsView, RequisitesView, BaseRegisterView, search, sort, start_seed


urlpatterns = [
    path('', ApplicationsView.as_view(), name='application'),
    path('requisites/', RequisitesView.as_view(), name='requisites'),
    path('search/', search, name='search'),
    path('sort/', sort, name='sort'),
    path('start_seed/', start_seed, name='start_seed'),
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
]