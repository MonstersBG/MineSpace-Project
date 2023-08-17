from django.urls import path
from .views import ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns = [
    path('details/', ProfileDetailsView.as_view(), name="profile_details"),
    path('edit/', ProfileEditView.as_view(), name="profile_edit"),
    path('delete/', ProfileDeleteView.as_view(), name="profile_delete"),
]
