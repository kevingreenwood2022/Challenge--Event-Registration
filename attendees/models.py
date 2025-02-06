from django.db import models

# Create your models here.
class Participant(models.Model):
    SESSION_CHOICES = [
        ('session_morning', 'Morning Session'),
        ('session_afternoon', 'Afternoon Session'),
        ('session_evening', 'Evening Session'),
        ('session_night', 'Night Session'),
    ]

    DIET_CHOICES = [
        ('none', 'No Preference'),
        ('veg', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gf', 'Gluten-Free'),
        ('df', 'Dairy-Free'),
        ('nf', 'Nut-Free'),
        ('allergies', 'Allergies'),
        ('other', 'Other'),
        ('vegan_gf', 'Vegan and Gluten-Free'),
        ('vegan_df', 'Vegan and Dairy-Free'),
        ('vegan_nf', 'Vegan and Nut-Free'),
        ('vegan_allergies', 'Vegan and Allergies'),
        ('vegan_other', 'Vegan and Other'),

    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    sessions = models.CharField(max_length=20, choices=SESSION_CHOICES)
    dietary = models.CharField(max_length=20, choices=DIET_CHOICES)

    def __str__(self):
        return self.name