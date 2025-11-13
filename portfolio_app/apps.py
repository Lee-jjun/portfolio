from django.apps import AppConfig
from django.urls import path
from . import views

class PortfolioAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio_app'

urlpatterns = [
    path('', views.home, name='home'),
]