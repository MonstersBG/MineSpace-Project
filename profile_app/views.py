from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import UserEditForm

AppUser = get_user_model()


class ProfileDetailsView(views.DetailView):
    template_name = 'profile/profile-details.html'
    model = AppUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        primary_key = self.request.GET.get('pk')
        user = AppUser.objects.filter(pk=primary_key).first()
        context['user'] = user
        return context


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/profile-edit.html'
    model = AppUser
    form_class = UserEditForm
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = AppUser

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context

