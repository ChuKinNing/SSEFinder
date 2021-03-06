from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # case
    path('cases/', views.CaseListView.as_view(), name='cases'),
    path('case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    path('case/create/', views.CaseCreate.as_view(), name='case-create'),
    path('case/<int:pk>/update/', views.CaseUpdate.as_view(), name='case-update'),
    path('case/<int:pk>/delete/', views.CaseDelete.as_view(), name='case-delete'),
    path('event/case/<int:pk>/update/', views.CaseUpdate.as_view(), name='case-update'),
    # location
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('location/create/', views.LocationView, name='location-create'),
    path('location/<int:pk>/delete/', views.LocationDelete.as_view(), name='location-delete'),
    # event
    path('events/',views.EventListView.as_view(),name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
    path('events/create/', views.EventCreate.as_view(), name='event-create'),
    path('event/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('case/event/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', views.EventDelete.as_view(), name='event-delete'),
    path('location/event/<int:pk>/update/', views.EventUpdate.as_view(), name='event-update'),
    # attend
    path('attend/create/', views.AddAttend, name='attend-create'),
    path('case/attend/<int:pk>/delete/', views.AttendDelete.as_view(), name='attend-delete'),
    path('event/attend/<int:pk>/delete/', views.AttendDelete.as_view(), name='attend-delete'),
    # SSE
    path('sse/select/', views.SelectSse, name = 'sse-select'),
    #Search
    path('cases/caseSearch/', views.caseSearchView.as_view(),name='case-search'),
    path('event/search/', views.EventSearch,name='event-search'),
    path('location/search/', views.LocationSearch,name='location-search'),
]
