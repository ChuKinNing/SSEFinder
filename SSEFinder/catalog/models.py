from django.db import models
import uuid # required for unique attend
from django.urls import reverse

# redundunt, because django already provided today, but can take it as reference for date format
# from datetime import date
# today_date = date.today().strftime('%Y-%m-%d')

# Create your models here.
class Case(models.Model):
    """Model for Case."""
    case_id = models.IntegerField(default=0, help_text='Unique ID of the case', unique=True)
    HKID = models.CharField(max_length=30, null=True, help_text='Enter Identity Document Number of the case (e.g. A123456(7) )', unique=True)
    name = models.CharField(max_length=100, null=True, help_text='Enter name of the patient (e.g. Chan Tai Man)')
    date_of_birth = models.DateField(null=True, help_text='Enter the date of birth of the patient')
    date_of_onset = models.DateField(null=True, help_text='Enter the date of onset of the patient')
    date_of_confirmed = models.DateField(null=True, help_text='Enter the date of positive confirmation of the patient')

    class Meta:
        ordering = ['case_id']

    def __str__(self):
        """String for representing the Case"""
        return f'{self.case_id}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this case."""
        return reverse('case-detail', args=[str(self.id)])

class Location(models.Model):
    """Model for location"""
    name = models.CharField(max_length=1000, null=True, help_text='Enter name of the location')
    venue_location = models.CharField(max_length=200, null=True, help_text='Enter the location')
    address = models.CharField(max_length=200, null=True, help_text='Enter the address')
    x_coordination = models.FloatField(null=True, help_text='Enter X cordinate of the location')
    y_coordination = models.FloatField(null=True, help_text='Enter Y cordinate of the location')

    class Meta:
        ordering = ['venue_location']

    def __str__(self):
        return self.venue_location

    def get_absolute_url(self):
        """Returns the url to access a detail record for this location."""
        return reverse('location-detail', args=[str(self.id)])


class Attend(models.Model):
    case = models.ForeignKey('Case', on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)

    ROLE = (
        ('a', 'possible infector'),
        ('b', 'possibly infected'),
        ('c', 'both'),
        ('d', 'none')
    )

    status = models.CharField(
        max_length=1,
        choices=ROLE,
        blank=True,
        default='d',
        help_text="Patient's role in event",
    )

    class Meta:
        ordering = ['case', 'event', 'status']

    def __str__(self):
        return f'{self.case.case_id} ({self.event.event_name})'

class Event(models.Model):
    # event_name = models.CharField(max_length=200, null=True, help_text='Enter name of the event')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True, help_text='Date of the eventm e.g. YYYY-MM-DD')

    class Meta:
        ordering = ['location', 'date']

    def get_absolute_url(self):
        """Returns the url to access a detail record for this event."""
        return reverse('event-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.location.venue_location} ({self.date})'




class SSE(models.Model):
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['event']

    def __str__(self):
        return f'{self.event.location.name} ({self.event.date})'
