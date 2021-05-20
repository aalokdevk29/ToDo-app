from django.db import models

from django.utils import timezone

STATUS_CHOICES = (
    ("Start", "start"),
    ("Hold", "hold"),
)


class Category(models.Model):
    """Category Model."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Todo(models.Model):
    """Todo Model."""

    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default='start'
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='todo_category', on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title