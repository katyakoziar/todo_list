from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class CustomBooleanField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [(True, 'Done'), (False, 'Not Done')]
        super().__init__(*args, **kwargs)


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField()
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = CustomBooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["-is_completed", "-created_at"]

    def __str__(self):
        return f"{self.content} {self.is_completed}"
