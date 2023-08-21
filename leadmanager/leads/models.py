from django.db import models
from django.contrib.auth.models import User
""" 
The User model is a built-in model provided by Django's authentication system,
and it's used for managing user accounts, authentication, and authorization in your
Django application.

With the User model, you can perform various operations related to user management,
such as user registration, login, password management, and more.

The model comes with fields like username, email, and password, as well as methods
for handling authentication and authorization.

Remember that while the built-in User model provides basic user management
functionality, in more complex applications, you might need to extend or customize
the user model to include additional fields or behaviors. 

This is typically done by creating a custom user model that inherits from AbstractUser
or AbstractBaseUser classes provided by Django's authentication framework
"""

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    owner = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

"""
owner: This field represents the owner of the lead and is related to the User model.

It's a foreign key, indicating a many-to-one relationship between Lead and User
models. The related_name attribute allows you to access leads associated with a user
using the attribute name on the User model. The on_delete=models.CASCADE indicates
that when a user is deleted, their associated leads will be deleted as well. The
null=True allows the owner field to be optional.
"""

# migrate any time you change your models
"""
'python manage.py makemigrations'--> This command is used to generate new database
migration files based on changes in your models.

'python manage.py migrate' --> This command is used to apply the generated migrations
and update your database schema to match your models. 

This process ensures that your database schema is synchronized with the changes
you've made to your models.
"""