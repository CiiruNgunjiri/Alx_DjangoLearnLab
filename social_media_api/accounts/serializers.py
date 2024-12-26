from rest_framework import serializers
from .models import CustomUser  # Adjust this import based on your user model
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

UserModel = get_user_model()  # Store the user model for reuse

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel  # Use the custom user model configured in settings
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserModel(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()

        # Automatically create a token for the new user
        Token.objects.create(user=user)

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = UserModel.objects.get(username=data['username'])
            if not user.check_password(data['password']):
                raise serializers.ValidationError("Invalid username or password.")
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("User does not exist.")

        return data

# Note: The token retrieval should typically be handled in the view, not here.
