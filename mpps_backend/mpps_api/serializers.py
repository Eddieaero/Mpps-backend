from rest_framework import serializers
from .models import *

class BusinessLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLicense
        fields = '__all__'  # Include all fields

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # fields = ('first_name', 'last_name',  'company_name','address','email', 'phone_number', 'password',  'is_admin')  # Customize fields
#         fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'company_name', 'address', 'phone_number', 'is_active', 'is_staff']
        extra_kwargs = {
            'password': {'write_only': True},  # Password should not be included when serializing
        }

    def create(self, validated_data):
        # Create and return a new CustomUser instance using the validated data
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        # Update and return an existing CustomUser instance using the validated data
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        
        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        instance.save()
        
        return instance



class BusinessLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessLicense
        fields = ['CustomUser', 'license_number', 'business_name', 'document', 'verified']

class TransitPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitPass
        fields = ['CustomUser', 'license_number', 'transit_pass_id', 'start_point', 'end_point', 'start_date', 'end_date', 'driver_number', 'vehicle_number', 'cargo_type', 'specie', 'length', 'width', 'breadth', 'quantity', 'transit_pass_document']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['CustomUser', 'amount', 'description', 'status', 'created_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['transaction', 'payment_method', 'payment_id', 'payment_time']

###################################################################
####################################################################

class CheckpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkpoint
        fields = ['code', 'name', 'latitude', 'longitude']

class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = ['journey_id', 'start_point', 'end_point', 'route']