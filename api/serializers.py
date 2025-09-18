from rest_framework import serializers
from .models import Course, Channel, Rate
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ["pk","username","password"]
            extra_kwargs = {'password': {'write_only':True, 'required':True}}

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["pk","title","channel","link","details","image","rating_num","avg_rating"]


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"