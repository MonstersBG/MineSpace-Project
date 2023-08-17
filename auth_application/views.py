from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import RegistrationForm
from django.utils.http import url_has_allowed_host_and_scheme


# Create your views here.

class RegisterView(views.CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy("login")


class LoginView(auth_views.LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        next_url = self.request.GET.get("next")

        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts=None):
            return next_url

        return reverse_lazy('home')


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = "home"
