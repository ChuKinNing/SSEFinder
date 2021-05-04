from django.shortcuts import render
from catalog.models import Case, Attend, Event, Location, SSE
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

import requests
from .forms import LocationForm, AttendForm

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
    Attend.objects.filter(case=None).delete()
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
    # when the request is post
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
                # data retrieve is successful
                if response.status_code == 200:
                    retrieved_data = json.loads(response.text)
                    extracted_data = retrieved_data
                    # more than one location or zero location is returned
                    if len(extracted_data) > 1 or len(extracted_data) == 0:
                         context = {}
                         return render(request, 'location_after_input.html', context = context)
                    # correct location is returned (only one)
                    else:
                        extracted_data = retrieved_data[0]
                        context = {
                            "name": name,
                            "address": extracted_data["addressEN"],
                            "venue_location": extracted_data["nameEN"],
                            "x_coordination": extracted_data["x"],
                            "y_coordination": extracted_data["y"],
                                }
                        location = Location.objects.create(**context)
                        return render(request, 'location_after_input.html', context = context)
            # when the request is get
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
    # remove relatate object to Foreign key object
    Event.objects.filter(location=None).delete()
    success_url = reverse_lazy('locations')

class EventListView(generic.ListView):
    model = Event

class EventDetailView(generic.DetailView):
    model = Event

class EventCreate(CreateView):
    model = Event
    fields = '__all__'

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(DeleteView):
    model = Event
    SSE.objects.filter(event=None).delete()
    Attend.objects.filter(event=None).delete()
    success_url = reverse_lazy('events')

def AddAttend(request):
    form = AttendForm(None)
    context = {
    'form':form,
    }
    # when the request is post
    if request.method == 'POST':
        form = AttendForm(request.POST or None)
        if form.is_valid():
            case_selected = form.cleaned_data['case']
            event_selected = form.cleaned_data['event']

            # set initial status = none
            calculated_status='d'

            # distinguish the role of the case in the event

            # incubation period
            if (event_selected.date >= (case_selected.date_of_onset - timedelta(days=14))) and (event_selected.date <= (case_selected.date_of_onset - timedelta(days=2))):
                calculated_status = 'b'

            # infectious period
            if (event_selected.date >= (case_selected.date_of_onset - timedelta(days=3))) and (event_selected.date <= case_selected.date_of_confirmed):
                calculated_status = 'a'

            # both
            if (event_selected.date >= (case_selected.date_of_onset - timedelta(days=14))) and (event_selected.date <= (case_selected.date_of_onset - timedelta(days=2))) and (event_selected.date >= (case_selected.date_of_onset - timedelta(days=3))) and (event_selected.date <= case_selected.date_of_confirmed):
                calculated_status = 'c'
            new_attend = Attend.objects.create(case=case_selected, event=event_selected, status=calculated_status)

            context = {}
            return render(request, 'attend_success.html', context = context)
        # if the form is not valid, aka has exception
        else:
            context = {
            'form':form,
            }
            return render(request, 'attend_form.html', context = context)
    # when the reqeust is get
    else:
        context = {
        'form':form,
        }
        return render(request, 'attend_form.html', context = context)
    return render(request, 'attend_form.html', context = context)
