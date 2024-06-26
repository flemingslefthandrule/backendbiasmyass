from rest_framework import serializers 
from user.models import User 


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('displayname', 'username', 'password', 'bio', 'image')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(
            **validated_data
        )
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User 
        fields = ('username', 'bio', 'image')
    
    def get_reviews():
        pass


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)