from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead viewset
class LeadViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = LeadSerializer

    def get_queryset(self):
        """
        returns a queryset of leads associated with the user
        making the request.

        'self.request.user'--> This represents the currently
        authenticated user who is making the request.
        
        If the user is not authenticated, this would be an
        instance of AnonymousUser.
        """
        return self.request.user.leads.all()
    
    def perform_create(self, serializer):
        """
        when a new object is being created using this view or viewset,
        the perform_create method is called. This method uses the provided
        serializer to save the incoming data as a new object while also setting
        the owner field of that object to the currently authenticated user.

        This approach is often used for scenarios where you want to automatically
        associate the authenticated user with any new objects they create,
        ensuring proper ownership and authorization controls.

        'serializer.save(owner=self.request.user)'--> This line of code
        saves the serialized data into an object, likely a model instance.
        
        Let's break down this line further:
        'serializer'--> This is an instance of a serializer class responsible
        for validating and deserializing the incoming data. It takes the input
        data and converts it into a format that can be used to create or
        update a model instance.

        '.save(owner=self.request.user)'--> This method call saves the serialized
        data as a new object in the database. Additionally, it assigns the
        currently authenticated user (self.request.user) to the owner field of
        the object being created.
        """
        serializer.save(owner=self.request.user)