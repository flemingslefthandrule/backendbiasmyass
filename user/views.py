from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from user.models import User
from user.serializers import UserSerializer

@api_view(['POST'])
def signup(request):

@api_view(['POST',])
def login(request):
        

class UserView(views.APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, format=None, pk=None):
        user = self.request.user
        user_data = request.data.get('user')
        
        user.displayname = user_data['displayname'] 
        user.bio = user_data['bio']
        user.image = user_data['image']
        user.save()
        
        serializer = UserSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)