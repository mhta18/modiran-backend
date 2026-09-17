from django.db import models


class Solution(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=20, blank=True)
    features = models.JSONField(default=list, blank=True)
    image_url = models.URLField(blank=True)
    link = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    link = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructor = models.CharField(max_length=200, blank=True)
    image_url = models.URLField(blank=True)
    link = models.URLField(blank=True)
    duration = models.CharField(max_length=100, blank=True)
    course_type = models.CharField(max_length=100, blank=True)
    level = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=200, blank=True)
    summary = models.TextField(blank=True)
    content = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title


class Media(models.Model):
    MEDIA_TYPES = [
        ("video", "Video"),
        ("podcast", "Podcast"),
        ("interview", "Interview"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    thumbnail_url = models.URLField(blank=True)
    media_url = models.URLField()
    duration = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    company = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    image_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.name
