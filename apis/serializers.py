# Include Serializers from DRF
from rest_framework import serializers


# Create a new class based the serializer class from DRF
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # Define the serializers and specify the fields to accept

    name = serializers.CharField(max_length=10)