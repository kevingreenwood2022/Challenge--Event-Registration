from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Participant
from .forms import RegistrationForm

# Create your views here.
class RegistrationView(CreateView):
    model = Participant
    form_class = RegistrationForm
    template_name = 'attendees/registration_form.html'
    success_url = reverse_lazy('list_view')

class ListViewParticipants(ListView):
    model = Participant
    template_name = 'attendees/participants_list.html'
    context_object_name = 'participants'

class EditView(UpdateView):
    model = Participant
    form_class = RegistrationForm
    template_name = 'attendees/edit_participant.html'
    success_url = reverse_lazy('list_view')

class RemoveView(DeleteView):
    model = Participant
    template_name = 'attendees/confirm_delete.html'
    success_url = reverse_lazy('list_view')