from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):

    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(max_length=200)

    position = models.CharField(max_length=200)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.company_name