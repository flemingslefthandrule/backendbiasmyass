from rest_framework import serializers
from django.contrib.auth import get_user_model
from author.models import Author


User = get_user_model()
    
class AuthorSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(read_only=True, many=True)
    
    class Meta:
        model = Author
        fields = ['slug','name','summary','work','photo', 'bio','reviews','url']