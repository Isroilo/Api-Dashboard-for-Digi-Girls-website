from rest_framework import serializers
from .models import *


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class About_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Info
        fields = "__all__"

class About_ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Project
        fields = "__all__"

class Courses_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_Info
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class Task_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_info
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = "__all__"

class Result_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result_info
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"