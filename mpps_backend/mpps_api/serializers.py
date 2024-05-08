from rest_framework import serializers
from .models import BusinessLicense, User, TransitPass, Payment  # Import your models

class BusinessLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLicense
        fields = '__all__'  # Include all fields

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'company_name', 'phone_number', 'address', 'is_admin')  # Customize fields

class TransitPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitPass
        fields = '__all__'  # Include all fields

# Add serializer for Payment if needed (similar to others)
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'  # Customize fields as needed
