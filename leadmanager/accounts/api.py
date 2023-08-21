"""
API implementation for user registration, login, and retrieving user information.

The code utilizes the generics module for views and permissions for access control,
and also includes the use of the knox library for token-based authentication.
"""
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    """This class handles user registration through the API."""

    serializer_class = (
        RegisterSerializer  # serializer to use for handling registration data.
    )

    def post(self, request, *args, **kwargs):
        """
        handles the HTTP POST request for user registration.

        the provided registration data is deserialized using the serializer.

        If the deserialization is successful (the data is valid), a new user
        is created using the serializer's save method.

        The response includes the serialized user data and a token generated
        using 'AuthToken.objects.create(user)' from the knox library.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        """
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)
        })

        I get the error when testing API with postman:
        TypeError: Object of type AuthToken is not JSON serializable
        """
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User registered successfully",
                "token": token,
            }
        )


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User login successfull",
                "token": token,
            }
        )


# Get_user API
class UserAPI(generics.RetrieveAPIView):
    """This class defines a view for retrieving user information."""

    permission_classes = [
        permissions.IsAuthenticated,
    ]
    """
    This specifies that only authenticated users are allowed to access
    this view. The IsAuthenticated permission class ensures that only
    logged-in users can access this endpoint.
    """
    serializer_class = UserSerializer

    def get_object(self):
        """
        returns the currently authenticated user. By using 'self.request.user',
        you're accessing the user associated with the current request.
        """
        return self.request.user
