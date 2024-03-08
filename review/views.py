from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404

from review.models import Review
from review.serializers import ReviewSerializer
from author.models import Author

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
    permission_classes=[IsAuthenticated]

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]

        return super().get_permissions()

    def get(self, slug):
        if slug:
            author = get_object_or_404(Author, slug=slug)
            return Review.objects.filter(author=author)
        return Review.objects.all()

    def post(self, request, slug):
        try:
            author = get_object_or_404(Author, slug=slug)
            review_data = request.data
            serializer_context = {'author': author}
            serializer = self.get_serializer(data=review_data, context=serializer_context)

            if serializer.is_valid():
                serializer.save()
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

            else:
                return Response({
                    "errors": {
                        "body": serializer.errors
                    }
                }, status=status.HTTP_400_BAD_REQUEST)
                
        except Exception as e:
            return Response({
                "errors": {
                    "body": [str(e)]
                }
            }, status=status.HTTP_400_BAD_REQUEST)