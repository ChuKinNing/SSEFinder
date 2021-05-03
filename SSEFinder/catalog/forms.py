from django.forms import ModelForm
from catalog.models import Location
from django.utils.translation import ugettext_lazy as _

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        labels = {'name': _('Venue name')}
        help_texts = {'name': _('Enter a venue name')}
