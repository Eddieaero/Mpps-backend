from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import BusinessLicense, User, TransitPass, Payment
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

class RegisterView(View):
    @APIView
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'message': 'User registered successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
class UploadView(View):
    @APIView
    def post(self, request, *args, **kwargs):
        document = request.FILES['document']
        business_license = BusinessLicense(document=document)
        business_license.save()
        return JsonResponse({'message': 'File uploaded successfully'})
    
class TransitPassForm(forms.ModelForm):
    class Meta:
        model = TransitPass
        fields = '__all__'

class TransitPassView(View):
    
    def post(self, request, *args, **kwargs):
        form = TransitPassForm(request.POST)
        if form.is_valid():
            transit_pass = form.save()
            return JsonResponse({'message': 'Transit pass created successfully'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)


