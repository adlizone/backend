from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from .models import UserProfile
class CustomLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
        max_length=10,
        required=True,
        validators = [] #use phone number validator here
    )
    password = serializers.CharField(write_only=True)

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

class RegisterSerializer(serializers.ModelSerializer):

    phone_number = serializers.CharField(
        required = True,
        max_length = 10,
        validators = []
    )
    password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['phone_number', 'password', 'repeat_password']
    
    def validate_phone_number(self, phone_number):
        """
        code to check if the user with the given username
        already exists in the database.
        """
        users = User.objects.all()
        usernames = [_.username for _ in users]
        if phone_number in usernames:
            raise serializers.ValidationError(_("username already exists."))
        return phone_number

    
    def validate_password(self, password):
        return password
    

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def save(self):
        # Create user with phone number and password
        user = User.objects.create(
            username=self.validated_data['phone_number'],
        )
        user.set_password(self.validated_data['password'])
        user.save()

        """
        Create an instance of the profile model for the new user.
        """

        UserProfile.objects.create(user=user)
       
        # Send OTP here for phone number verification

        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'