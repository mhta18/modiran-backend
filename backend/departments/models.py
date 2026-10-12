from django.db import models


class Department(models.Model):
    key = models.CharField(max_length=100, unique=True)  # e.g., 'management', 'hr'
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Update your Course model to link to Department
class Course(models.Model):
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="courses",
        null=True,
        blank=True,
    )
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
