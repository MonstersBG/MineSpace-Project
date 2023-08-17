from django.urls import path
from .views import help_ticket

urlpatterns = [
    path("", help_ticket, name="help"),

]
