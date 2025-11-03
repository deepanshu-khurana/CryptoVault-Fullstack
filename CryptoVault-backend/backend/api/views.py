# CryptoVault-backend\backend\api\views.py

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Standard DRF imports
from rest_framework import viewsets
from rest_framework.response import Response
from .models import SecureFile
from .serializers import SecureFileSerializer

# The following code is for the file upload API endpoint only.
@method_decorator(csrf_exempt, name='dispatch')
class SecureFileViewSet(viewsets.ModelViewSet):
    """
    API endpoint for handling secure file uploads (POST) and listing (GET).
    This uses Django's built-in file handling via the Model.
    """
    # Disables session authentication to fix the 403 CSRF error
    authentication_classes = [] 
    
    queryset = SecureFile.objects.all().order_by('-uploaded_at')
    serializer_class = SecureFileSerializer
    
    # This method is called upon POST request and saves the file via the Model.
    def perform_create(self, serializer):
        # The serializer handles the file saving to MEDIA_ROOT
        serializer.save()