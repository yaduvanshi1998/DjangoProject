from .models import UserDetails
from rest_framework import serializers # type: ignore

class UserDetailsSerializer(serializers.ModelSerializer):
    Email = serializers.EmailField(required=True) # used this to remove the default drf and print custom errors since unique=True in email field inside the model
    class Meta:
        model = UserDetails
        fields = '__all__' # To consider all the attributes in the model

    def validate_username(self, value):
        if UserDetails.objects.filter(Username=value).exists():
            raise serializers.ValidationError("User with this username already exists!")
        return value

    def validate_email(self, value):
        if UserDetails.objects.filter(Email=value).exists():
            raise serializers.ValidationError("User with this email already exists!")
        return value
