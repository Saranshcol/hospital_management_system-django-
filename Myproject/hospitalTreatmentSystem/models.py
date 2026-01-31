from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        PATIENT = 'Patient', 'Patient'
        DOCTOR = 'Doctor', 'Doctor'
        ADMIN = 'Admin', 'Admin'

    email = models.EmailField(max_length=100, unique=True)
    name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=15,
        choices=RoleChoices.choices,
        default=RoleChoices.PATIENT,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    
class Appointment(models.Model):
    class StatusChoices(models.TextChoices):
        SCHEDULED = 'Scheduled'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'
    patient = models.ForeignKey(User, related_name="patient_appointments", on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, related_name="doctor_appointments", on_delete=models.CASCADE)
    appointment_date = models.DateField()
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.SCHEDULED)
    
    
class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    treatment = models.ManyToManyField(Treatment)
    notes = models.TextField(blank=True)


#  Relationships

#  Appointment → User (patient & doctor as FK)
#  Prescription → Appointment (FK)
#  Prescription → Treatment (ManyToMany)

# data structures
# oops concepts
# ai concepts
# famous reasoning question