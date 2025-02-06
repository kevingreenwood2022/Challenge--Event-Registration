from django import forms
from .models import Participant

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'phone', 'sessions', 'dietary']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'sessions': 'Session Preference',
            'dietary': 'Dietary Preference',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Participant.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email