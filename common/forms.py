from django import forms
from .models import HelpTickets


class HelpTicketForm(forms.ModelForm):
    class Meta:
        model = HelpTickets
        fields = ["title", "description", ]
