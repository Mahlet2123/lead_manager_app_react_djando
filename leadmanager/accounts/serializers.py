"""
This code is responsible for validating and handling the
registration process of new users.
"""
from rest_framework import serializers;
"""
imports the necessary classes and functions from the
Django REST framework for creating serializers.
"""
from django.contrib.auth.models import User;
"""
imports the built-in User model provided by Django for
user authentication and authorization.
"""
from django.contrib.auth import authenticate;
"""
imports the authenticate function from Django's
authentication module.
"""

# User serializer
class UserSerializer(serializers.ModelSerializer):
    """ used to serialize user data """
    class Meta:
        """
        defines the model (User) and the fields that should be
        included in the serialized output.
        """
        model = User
        fields = ('id', 'username', 'email')

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        """
        extra_kwargs --> are used to provide additional options for the fields.
        
        In this case, the password field is marked as write_only, which means
        it won't be included in the serialized output.
        
        This is a common practice for security reasons, as you don't want to
        expose the password in the API responses.
        """

    def create(self, validated_data):
        """
        This method overrides the default create method of the serializer to
        handle the user creation process.
        
        It takes validated_data as an argument, which contains the validated
        and cleaned input data.
        
        Inside the create method, a new user is created using 'User.objects.create_user'
        method, passing in the validated username, email, and password data.
        
        The create_user method takes care of hashing the password and saving the
        user object to the database.
        
        Finally, the newly created user is returned.
        """
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

# Login serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")