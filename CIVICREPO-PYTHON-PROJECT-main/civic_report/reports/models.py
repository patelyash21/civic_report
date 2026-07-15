from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    CATEGORY_CHOICES = [
        ('Road Issue', 'Road Issue'),
        ('Garbage', 'Garbage'),
        ('Water Leakage', 'Water Leakage'),
        ('Electricity', 'Electricity'),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    location = models.CharField(max_length=255)

    latitude = models.FloatField(null=True,blank=True)

    longitude = models.FloatField(null=True,blank=True)

    image = models.ImageField(
        upload_to='reports/',
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title