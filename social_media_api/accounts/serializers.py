from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

UserModel = get_user_model()  # Get the user model

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel  # Use the custom user model configured in settings
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user using the create_user method
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
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

    def create(self, validated_data):
        username = validated_data['username']
        user = UserModel.objects.get(username=username)
        
        # Create or get the token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        return {'token': token.key}
