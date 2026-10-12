from rest_framework import serializers

from .models import (
    Solution,
    Book,
    News,
    Feedback,
)


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = [
            "id",
            "icon",
            "title",
            "description",
            "features",
            "image_url",
            "link",
            "is_active",
            "order",
            "created_at",
            "updated_at",
        ]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "category",
            "description",
            "image_url",
            "link",
            "is_active",
            "created_at",
            "updated_at",
        ]

class NewsSerializer(serializers.ModelSerializer):
    excerpt = serializers.CharField(source="summary", required=False, allow_blank=True)

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "category",
            "published_at",
            "excerpt",
            "content",
            "image_url",
            "is_published",
            "created_at",
            "updated_at",
        ]

class FeedbackSerializer(serializers.ModelSerializer):
    text = serializers.CharField(source="message")

    class Meta:
        model = Feedback
        fields = [
            "id",
            "name",
            "role",
            "company",
            "text",
            "image_url",
            "is_active",
            "order",
            "created_at",
        ]
