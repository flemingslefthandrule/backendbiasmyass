from rest_framework import viewsets , status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response 

from user.models import User
from author.models import Author
from author.serializers import AuthorSerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 
    permission_classes=[IsAuthenticated]
    lookup_field='slug'
    http_method_names = ['get']
    
    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]

        return super().get_permissions()