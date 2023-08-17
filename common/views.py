from django.shortcuts import redirect, render

from forum.models import Forum
from .forms import HelpTicketForm


# Create your views here.

def help_ticket(request):
    if request.method == "POST":
        form = HelpTicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = HelpTicketForm()

    context = {
        "form": form,
    }

    return render(request, "help/ticket-help.html", context)



