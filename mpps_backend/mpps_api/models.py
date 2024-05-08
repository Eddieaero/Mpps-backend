from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils import timezone


class User(AbstractUser):
    company_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)

class BusinessLicense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)
    business_name = models.CharField(max_length=255)
    document = models.FileField(upload_to='business_licenses/')
    verified = models.BooleanField(default=False)

class TransitPass(models.Model):
    TRANSIT_TYPE_CHOICES = [
        ('hard_wood', 'Hard Wood'),
        ('soft_wood', 'Soft Wood'),
        ('wood_timber', 'Wood Timber'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_number = models.ForeignKey(BusinessLicense, on_delete=models.CASCADE)
    transit_pass_id = models.CharField(max_length=50)
    start_point = models.CharField(max_length=255)
    end_point = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    driver_number = models.CharField(max_length=50)
    vehicle_number = models.CharField(max_length=50)
    cargo_type = models.CharField(max_length=20, choices=TRANSIT_TYPE_CHOICES)
    specie = models.CharField(max_length=50)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    breadth = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    quantity = models.IntegerField()
    transit_pass_document = models.FileField(upload_to='transit_passes/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.end_date is None:
            self.end_date = self.start_date + timedelta(days=10)
        super().save(*args, **kwargs)

class Payment(models.Model):
    TRANS_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    transit_pass = models.ForeignKey(TransitPass, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=TRANS_STATUS_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    payment_number = models.CharField(max_length=50)
    payment_date = models.DateField(default=timezone.now)