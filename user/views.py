from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status, views, viewsets
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from user.serializers import UserSerializer, ProfileSerializer

@api_view(['POST'])
def signup(request):
    try:
        user_data = request.data.get('user')
        
        serializer = UserSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 

        return Response({"user": serializer.data}, status=status.HTTP_201_CREATED)
    
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
def login(request):
    try:
        user_data = request.data.get('user')
        user = authenticate(username=user_data['username'], password=user_data['password']) 

        serializer = UserSerializer(user)
        jwt_token = RefreshToken.for_user(user)
        serializer_data = serializer.data
        serializer_data['token'] = str(jwt_token.access_token)

        response_data = {
            "user": serializer_data,
        }

        return Response(response_data, status=status.HTTP_202_ACCEPTED)
    
    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        

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

class ProfileView(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'
    http_method_names = ['get', 'post', 'delete']
    
    def get_permissions(self):
        if self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]
        return super().get_permissions()
    
    def list(self, request, username=None, *args, **kwargs):
        try: 
            profile = User.objects.get(username=username)
            serializer = self.get_serializer(profile)
            return Response({"profile": serializer.data})

        except Exception:
            return Response({"errors": {
                "body": [
                    "invalid user"
                ]
            }})