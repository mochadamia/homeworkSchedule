from rest_framework import serializers
from .models import Assignment, ClassName, Comment


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = '__all__'


class CommentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment


class AssignmentSerializer(serializers.ModelSerializer):
    class_id = ClassSerializer(read_only=True)
    class_name_id = serializers.PrimaryKeyRelatedField(
        queryset=ClassName.objects.all(),
        write_only=True,
        required=True,
    )
    comments = CommentSimpleSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name', 'content', 'class_id', 'class_name_id', 'comments')
        model = Assignment

    def create(self, validated_data):
        class_id = validated_data.pop('class_name_id')
        return Assignment.objects.create(class_id=class_id, **validated_data)


class CommentSerializer(serializers.ModelSerializer):
    assignment_id = AssignmentSerializer(read_only=True)
    assignment = serializers.PrimaryKeyRelatedField(
        queryset=Assignment.objects.all(),
        write_only=True,
        required=True,
    )

    class Meta:
        fields = ('id', 'content', 'assignment_id', 'assignment')
        model = Comment

    def create(self, validated_data):
        assignment_id = validated_data.pop('assignment')
        return Comment.objects.create(assignment_id=assignment_id, **validated_data)


