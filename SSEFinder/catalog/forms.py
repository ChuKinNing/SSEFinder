from django.forms import ModelForm
from catalog.models import Location
from django.utils.translation import ugettext_lazy as _
import requests
import json

class LocationForm(ModelForm):
    # def clean_venue_location(self):
    #     location = self.cleaned_data['venue_location']
    #     # check if it can be access by api
    #     try:
    #         location.replace(" ", "%20")
    #         url = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=" + location
    #         response = requests.get(url)
    #
    #         case_data = []
    #
    #         if response.status_code == 200:
    #             data = json.loads(response.text)
    #             case_data.append(data)
    #             print(data)
    #     except:
    #         raise ValidationError(_('Cannot search this place'))
        #
        #
        # return data
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
