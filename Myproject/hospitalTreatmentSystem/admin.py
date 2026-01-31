from django.contrib import admin
from .models import User, Appointment, Treatment, Prescription


admin.site.register(User)
admin.site.register(Appointment)
admin.site.register(Treatment)
admin.site.register(Prescription)