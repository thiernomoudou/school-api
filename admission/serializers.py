from admission.models import Registration, Admission 
from rest_framework import serializers

from school.serializers import BatchSerializer
from department.serializers import DepartmentSerializer, ClasslevelSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class AdmissionSerializer(serializers.ModelSerializer):

    batch = BatchSerializer()
    registree = RegistrationSerializer()
    department = DepartmentSerializer()
    class_level = ClasslevelSerializer()

    class Meta:
        model = Admission
        fields = '__all__'