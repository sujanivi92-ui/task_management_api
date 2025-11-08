from django.db import models
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.status})"

# Create your models here.
