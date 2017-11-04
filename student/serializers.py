from rest_framework import serializers

from .models import Student, Exam, Grade, Payment
from admission.serializers import AdmissionSerializer
from department.serializers import SubjectSerializer


class StudentSerializer(serializers.ModelSerializer):
    student = AdmissionSerializer()
    class Meta:
        model = Student
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):

    exam = ExamSerializer()
    student = StudentSerializer()
    subject = SubjectSerializer()
    class Meta:
        model = Grade
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    student = StudentSerializer()
    class Meta:
        model = Payment
        fields = '__all__'
