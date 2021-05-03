from django.shortcuts import render
from catalog.models import Case, Attend, Event, Location
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


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
