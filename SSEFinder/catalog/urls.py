from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cases/', views.CaseListView.as_view(), name='cases'),
    path('case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    path('case/create/', views.CaseCreate.as_view(), name='case-create'),
    path('case/<int:pk>/update/', views.CaseUpdate.as_view(), name='case-update'),
    path('case/<int:pk>/delete/', views.CaseDelete.as_view(), name='case-delete'),
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
    path('locations/create/', views.LocationView, name='location-create'),
    # path('locations/create/', views.LocationCreate.as_view(), name='location-create'),
    # path('locations/<int:pk>/update/', views.LocationUpdate.as_view(), name='location-update'),
    path('locations/<int:pk>/delete/', views.LocationDelete.as_view(), name='location-delete'),
    path('events/',views.EventListView.as_view(),name='events'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='event-detail'),
]
