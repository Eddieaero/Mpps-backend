# Import the correct CustomUser from models.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class BusinessLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLicense
        fields = '__all__'

class TransitPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitPass
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = '__all__'
