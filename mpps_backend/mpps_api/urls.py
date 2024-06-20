from django.contrib import admin
from django.urls import path
from .views import *





urlpatterns = [

    path('login/', UserLoginView.as_view(), name='login'),  
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('uploadDocument/', UploadView.as_view(), name='upload'),
    # path('viewDocument/', ), ##i need to add here list of documents
    # path('viewDocumnet/<int:pk>/', DocumentView.as_view(), name='documents'),
    path('transitPassApplication/', TransitPassView.as_view(), name='transit-pass'),
    path('user-transit-passes/', UserTransitPassListView.as_view(), name='user-transit-passes'),
    path('user-transactions/', UserTransactionListView.as_view(), name='user-transactions'),


    # router.register(r'checkpoints', CheckpointViewSet)
    # router.register(r'journeys', JourneyViewSet)


]