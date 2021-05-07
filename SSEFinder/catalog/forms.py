from django.forms import ModelForm
from catalog.models import Location, Attend, Case, Event
from django.utils.translation import ugettext_lazy as _
import requests
import json

from datetime import datetime, timedelta
from datetime import date
from django.core.exceptions import ValidationError

from django import forms

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'venue_location']
        labels = {
            'name': _('Venue name'),
            'venue_location': _('Venue location')
        }
        help_texts = {
            'name': _('Enter the venue name'),
            'venue_location': _('Enter the venue location')
            }

class AttendForm(ModelForm):

    # raise exception for event that lies outside the desired period
    def clean_event(self):
        event = self.cleaned_data['event']
        case = self.cleaned_data['case']
        if event.date < (case.date_of_onset - timedelta(days=14)):
            raise ValidationError(_('Invalid date: event is before the incubation period'))
        if event.date > (case.date_of_confirmed):
            raise ValidationError(_('Invalid date: event is after the confirmation of positivity'))
        return event

    class Meta:
        model = Attend
        fields = ['case', 'event']
        labels = {
            'case': _('Case'),
            'event': _('Event')
        }
        help_text = {
            'case': _('Choose Case'),
            'event': _('Choose Event')
        }


class DateInput(forms.DateInput):
    input_type = 'date'

class SseDateForm(forms.Form):
    start_date = forms.DateField(help_text="Enter a beginning date of the desired period", widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(help_text="Enter a ending date of the desired period", widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        widgets = {
            'date_of_birth':  DateInput(),
            'date_of_onset': DateInput(),
            'date_of_confirmed': DateInput()
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }

class EventSearchForm(forms.Form):
    location_name=forms.CharField(label='Venue name', help_text="Enter the venue name", required = False)
    venue_location=forms.CharField(label='Venue location',help_text="Enter the venue location", required = False)
    date_from=forms.DateField(help_text="Enter a beginning date of the desired period", widget=forms.widgets.DateInput(attrs={'type': 'date'}), required = False)
    date_to=forms.DateField(help_text="Enter a ending date of the desired period", widget=forms.widgets.DateInput(attrs={'type': 'date'}), required = False)
