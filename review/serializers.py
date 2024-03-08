from rest_framework import serializers
from review.models import Review
from author.models import Author

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']

    def create(self, validated_data):
        author = self.context.get('author')
        review = Review.objects.create(author=author, **validated_data)
        return review