from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Appointment, Prescription, Treatment
from .serializers import (AppointmentSerializer, PrescriptionSerializer, TreatmentSerializer,)



class AppointmentListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["doctor", "status", "appointment_date"]

    def get_queryset(self):
        user = self.request.user

        if user.role == "Patient":
            return Appointment.objects.filter(patient=user)

        if user.role == "Doctor":
            return Appointment.objects.filter(doctor=user)

        return Appointment.objects.all()




class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.role == "Patient":
            return Appointment.objects.filter(patient=user)

        if user.role == "Doctor":
            return Appointment.objects.filter(doctor=user)

        return Appointment.objects.all()





class PrescriptionCreateView(generics.CreateAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "Doctor":
            raise PermissionError("Only doctors can create prescriptions.")

        serializer.save()
        
        
        
        
class PrescriptionListView(generics.ListAPIView):
    serializer_class = PrescriptionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["appointment"]

    def get_queryset(self):
        user = self.request.user

        if user.role == "Patient":
            return Prescription.objects.filter(appointment__patient=user)

        if user.role == "Doctor":
            return Prescription.objects.filter(appointment__doctor=user)

        return Prescription.objects.all()




class TreatmentListView(generics.ListAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = [IsAuthenticated]