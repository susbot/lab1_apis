# Include Serializers from DRF
from rest_framework import serializers
from apis import models


# Create a new class based the serializer class from DRF
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    # Define the serializers and specify the fields to accept

    name = serializers.CharField(max_length=10)


# Serializer for User Profile Object
# Model Serailizers needs a metaclass to configure and point to a specific model in project

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        # Specify a list of fields in model to manage through Serializer
        # Pass a tuple
        fields = ('id', 'email', 'name', 'password')
        # Password field WRITE ONLY
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # Overwrite the Create function in a ModelSerializer
    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
