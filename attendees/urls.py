from django.urls import path
from .views import RegistrationView, ListViewParticipants, EditView, RemoveView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register_view'),
    path('', ListViewParticipants.as_view(), name='list_view'),
    path('edit/<int:pk>/', EditView.as_view(), name='edit_view'),
    path('delete/<int:pk>/', RemoveView.as_view(), name='delete_view'),
]