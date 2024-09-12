from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class CustomLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True, validators=[validate_password])

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')

        if not phone_number or not password:
            raise serializers.ValidationError(_("Phone number and password are required."))

        # Authenticate the user using phone number and password
        user = authenticate(username=phone_number, password=password)  # DRF uses 'username' as a key for authentication
        if user is None:
            raise AuthenticationFailed(_("Invalid phone number or password"))

        if not user.is_active:
            raise AuthenticationFailed(_("User account is disabled"))

        # If authentication is successful, return the validated data and the user instance
        data['user'] = user
        return data

class CustomRegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    password = serializers.CharField(write_only=True, validators=[validate_password])
    repeat_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        """ 
        if User.objects.get(username=data['phone_number']) is not None:
            raise serializers.ValidationError({"username": "Username already exists."})
        """
        return data

    def save(self, request):
        # Create user with phone number and password
        user = User.objects.create(
            username=self.validated_data['phone_number'],
        )
        user.set_password(self.validated_data['password'])
        user.save()
        print(user)

        # Send OTP here for phone number verification

        return user
