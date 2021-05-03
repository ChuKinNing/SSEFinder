from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cases/', views.CaseListView.as_view(), name='cases'),
    path('case/<int:pk>', views.CaseDetailView.as_view(), name='case-detail'),
    path('case/create/', views.CaseCreate.as_view(), name='case-create'),
    path('case/<int:pk>/update/', views.CaseUpdate.as_view(), name='case-update'),
    path('case/<int:pk>/delete/', views.CaseDelete.as_view(), name='case-delete'),
]
