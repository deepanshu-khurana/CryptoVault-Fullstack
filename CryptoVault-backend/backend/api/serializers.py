# CryptoVault-backend\backend\api\serializers.py

from rest_framework import serializers
from .models import SecureFile

class SecureFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecureFile
        fields = ('id', 'file', 'blockchain_hash', 'uploaded_at')
        read_only_fields = ('uploaded_at',)