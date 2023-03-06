from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, UserProfile


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8)
    password_confirm = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('user with this email already exists')
        return email

    def validate(self, attrs):
        p1 = attrs['password']
        p2 = attrs.pop('password_confirm')
        if p1 != p2:
            raise serializers.ValidationError('password does not match')
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            # additional user fields here
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(min_length=6, write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.pop('password')
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User not found')
        user = authenticate(email=email, password=password)
        if user and user.is_active:
            refresh = self.get_token(user)
            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)
        else:
            raise serializers.ValidationError('Invalid password!')
        return attrs
    
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

