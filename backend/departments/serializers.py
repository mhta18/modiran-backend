from rest_framework import serializers
from .models import Department, Course


class CourseSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source="course_type", required=False, allow_blank=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "instructor",
            "duration",
            "type",
            "level",
            "description",
            "image_url",
            "link",
            "is_active",
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ["id", "key", "title", "description", "icon", "courses"]
