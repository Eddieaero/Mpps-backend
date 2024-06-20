from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django import forms
from django.http import JsonResponse


class UserRegistrationView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def get(self, request):
        users = CustomUser.objects.all()  # Replace 'User' with your actual user model
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)





class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    

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



class PaymentRequestView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can request payments

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, status='requested')  # Set user and status
            return Response({'message': 'Payment request created successfully'})
        else:
            return Response(serializer.errors, status=400)
        
class UserTransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(CustomUser=user)
    

class UserTransitPassListView(generics.ListAPIView):
    serializer_class = TransitPassSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TransitPass.objects.filter(CustomUser=user)
    

class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint.objects.all()
    serializer_class = CheckpointSerializer

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
