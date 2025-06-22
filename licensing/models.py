from django.db import models
from django.utils import timezone

class License(models.Model):
    LICENSE_TYPES = [
        ('trial', 'Trial (30 Days)'),
        ('monthly', 'Monthly Subscription'),
        ('yearly', 'Yearly Subscription'),
        ('lifetime', 'Lifetime Access'),
    ]

    license_type = models.CharField(max_length=20, choices=LICENSE_TYPES, default='trial')
    start_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def is_valid(self):
        return self.is_active and timezone.now().date() <= self.expiry_date

    def __str__(self):
        return f"{self.get_license_type_display()} - Expires on {self.expiry_date}"

