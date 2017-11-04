from rest_framework import serializers

from .models import ClassLevel, Department, Room, Subject


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ClasslevelSerializer(serializers.ModelSerializer):
    
    department = DepartmentSerializer()
    class Meta:
        model = ClassLevel
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):

    department = DepartmentSerializer()
    class Meta:
        model = Room
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):

    class_level = ClasslevelSerializer()
    teacher = serializers.StringRelatedField()
    class Meta:
        model = Subject
        fields = '__all__'
