from django.contrib import admin
from .models import Case, Location, Attend, Event, SSE

# Register your models here.

# define the admin class
@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_id', 'HKID', 'name', 'date_of_onset', 'date_of_confirmed')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'x_coordination', 'y_coordination')

@admin.register(Attend)
class AttendAdmin(admin.ModelAdmin):
    list_display = ('case', 'event', 'status')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'location', 'date')

@admin.register(SSE)
class SSEAdmin(admin.ModelAdmin):
    list_display = ('event',)
