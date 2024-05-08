from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import BusinessLicense, User, TransitPass, Payment
from .serializers import BusinessLicenseSerializer, UserSerializer, TransitPassSerializer, PaymentSerializer
from django.http import JsonResponse
from .serializers import BusinessLicenseSerializer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
import decorators






User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('company_name', 'phone_number', 'address', 'is_admin',)




from rest_framework.authtoken.views import obtain_auth_token

class LoginView(obtain_auth_token):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if not user.is_active:
                return Response({'error': 'Email is not verified'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

        return super().post(request, *args, **kwargs)

class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()  # Serializer handles saving the user
            return Response({'message': 'User registered successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
class UploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BusinessLicenseSerializer(data=request.POST)  # Assuming some fields in request.POST
        if serializer.is_valid():
            serializer.save()  # Serializer handles saving the license
            return Response({'message': 'File uploaded successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TransitPassForm(forms.ModelForm):
    class Meta:
        model = TransitPass
        fields = '__all__'

class TransitPassView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TransitPassSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()  # Serializer handles saving the pass
            return Response({'message': 'Transit pass created successfully'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
