from rest_framework import serializers
from .models import User, Appointment, Treatment, Prescription



class UserMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "name", "role")



class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ("id", "name", "description")



class AppointmentSerializer(serializers.ModelSerializer):
    patient = UserMiniSerializer(read_only=True)
    doctor = UserMiniSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = "__all__"



class PrescriptionSerializer(serializers.ModelSerializer):
    treatments = TreatmentSerializer(many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = "__all__"

    def validate(self, data):
        request = self.context.get("request")

        if request.user.role != "Doctor":
            raise serializers.ValidationError("Only doctors can create prescriptions.")

        if data["appointment"].status != "Completed":
            raise serializers.ValidationError("Appointment must be completed first.")

        return data
