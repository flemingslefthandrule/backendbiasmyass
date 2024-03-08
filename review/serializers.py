from rest_framework import serializers
from review.models import Review
from author.models import Author

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Review
        fields = ['author', 'text']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author = Author.objects.get(pk=author_data.pk)
        review = Review.objects.create(author=author, **validated_data)
        return review