from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #     return self._create_user(email, password, **extra_fields)
    
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'company_name', 'address', 'phone_number']

    def __str__(self):
        return self.email

class BusinessLicense(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=10)
        super().save(*args, **kwargs)

class Transaction(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    description = models.CharField(max_length=255)  # Description of the transaction
    status = models.CharField(max_length=50, choices=[  # Transaction status (requested, paid, etc.)
        ('requested', 'Requested'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ], default='requested')
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of transaction creation

    def __str__(self):
        return f"Transaction ID: {self.id} - User: {self.user.username} - Amount: {self.amount}"

class Payment(models.Model):
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)  # Related transaction
    payment_method = models.CharField(max_length=50, blank=True)  # Payment method used (e.g., credit card, debit card)
    payment_id = models.CharField(max_length=255, blank=True)  # Payment processor's transaction ID
    payment_time = models.DateTimeField(blank=True, null=True)  # Time of payment

    def __str__(self):
        return f"Payment for Transaction: {self.transaction.id} - Method: {self.payment_method}"

class Journey(models.Model):
    journey_id = models.CharField(max_length=50, unique=True)
    start_point = models.ForeignKey(TransitPass, related_name='start_journeys', on_delete=models.CASCADE)
    end_point = models.ForeignKey(TransitPass, related_name='end_journeys', on_delete=models.CASCADE)
    route = models.JSONField()  # Use JSONField to store a list of checkpoint codes in order

    def __str__(self):
        return f"Journey {self.journey_id} from {self.start_point.name} to {self.end_point.name}"
