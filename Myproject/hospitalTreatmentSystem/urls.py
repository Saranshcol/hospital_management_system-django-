from django.urls import path
from .views import (AppointmentListView, AppointmentRetrieveUpdateDestroyView, PrescriptionCreateView, 
    PrescriptionListView,
    TreatmentListView,
)

urlpatterns = [
    path("appointments/", AppointmentListView.as_view()),
    path("appointments/<int:pk>/", AppointmentRetrieveUpdateDestroyView.as_view()),

    path("prescriptions/", PrescriptionListView.as_view()),
    path("prescriptions/create/", PrescriptionCreateView.as_view()),

    path("treatments/", TreatmentListView.as_view()),
]
