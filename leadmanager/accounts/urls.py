""" urlpatterns configuration for Django URL routing. """
from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

"""
It sets up URL patterns for your authentication-related APIs
using Django's URL routing system and includes the knox
library's URL patterns for token-based authentication.

It includes the default knox URLs under the '/api/auth' path and
maps the '/api/auth/register' path to your RegisterAPI view for
user registration.
"""

urlpatterns = [
    path("api/auth", include("knox.urls")),
    path("api/auth/register", RegisterAPI.as_view()),
    path("api/auth/login", LoginAPI.as_view()),
    path("api/auth/user", UserAPI.as_view()),
    path("api/auth/logout", knox_views.LogoutView.as_view(), name="knox_logout"),
]
