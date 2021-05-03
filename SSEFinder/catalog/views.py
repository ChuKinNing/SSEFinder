from django.shortcuts import render
from catalog.models import Case, Attend, Event, Location
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import requests
from .forms import LocationForm

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

import requests
import json
import pprint
import sys
from datetime import date, timedelta


# Create your views here.
def index(request):
    """View function for home page of the site"""

    # Generate counts of some of the main objects
    num_case = Case.objects.all().count()
    num_location = Location.objects.all().count()
    num_event = Event.objects.all().count()

    context = {
        'num_case': num_case,
        'num_location': num_location,
        'num_event': num_event,
    }

    # return the HTML template index.html with the data in context
    return render(request, 'index.html', context=context)

class CaseListView(generic.ListView):
    model = Case

class CaseDetailView(generic.DetailView):
    model = Case

class CaseCreate(CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(UpdateView):
    model = Case
    fields = '__all__'

class CaseDelete(DeleteView):
    model = Case
    success_url = reverse_lazy('cases')

class LocationListView(generic.ListView):
    model = Location

class LocationDetailView(generic.DetailView):
    model = Location

class LocationCreate(CreateView):
    model = Location
    fields = ['name']


def LocationView(request):
    form = LocationForm(None)
    if request.method == 'POST':
        form = LocationForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            venue_location = form.cleaned_data['venue_location']
            try:
                venue_location.replace(" ", "%20")
                url = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=" + venue_location
                response = requests.get(url)
                case_data = []
                if response.status_code == 200:
                    retrieved_data = json.loads(response.text)
                    extracted_data = retrieved_data
                    if len(extracted_data) > 1 or len(extracted_data) == 0:
                         context = {}
                         return render(request, 'location_after_input.html', context = context)
                    else:
                        extracted_data = retrieved_data[0]
                        # if len(extracted_data) > 1:
                        #     return render(request, 'location_after_input.html', context = context)
                        context = {
                            "name": name,
                            "address": extracted_data["addressEN"],
                            "venue_location": extracted_data["nameEN"],
                            "x_coordination": extracted_data["x"],
                            "y_coordination": extracted_data["y"],
                                }
                        location = Location.objects.create(**context)
                        return render(request, 'location_after_input.html', context = context)
            except:
                context = {}
                return render(request, 'location_after_input.html', context = context)
    else:
        api_response = None
        context = {
        'form':form,
        }
        return render(request, 'location_form.html', context = context)




class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

class EventCreate(CreateView):
    model = Event
    fields = '__all__'
