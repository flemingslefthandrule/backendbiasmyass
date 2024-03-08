from rest_framework import serializers
from django.contrib.auth import get_user_model
from author.models import Author


User = get_user_model()
    
class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['url','name', 'photo', 'bio', 'reviews']