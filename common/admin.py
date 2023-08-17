from django.contrib import admin
from .models import HelpTickets

# Register your models here.


@admin.register(HelpTickets)
class HelpTicketsAdmin(admin.ModelAdmin):
    pass
