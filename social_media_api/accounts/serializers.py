from rest_framework import serializers
from .models import CustomUser  # Adjust this import based on your user model
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=data['username'])
            if not user.check_password(data['password']):
                raise serializers.ValidationError("Invalid credentials")
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("User does not exist")

        return data

    def create(self, validated_data):
        UserModel = get_user_model()
        user = UserModel.objects.get(username=validated_data['username'])
        
        # Create or get the token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        return {'token': token.key}
