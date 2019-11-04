from rest_framework import serializers
from .models import Assignment, Class, Comment


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Assignment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment


