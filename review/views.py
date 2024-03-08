from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status, generics

from review.models import Review
from review.serializers import ReviewSerializer
from author.models import Author

class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
    permission_classes=[IsAuthenticated]

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'list':
            return [IsAuthenticatedOrReadOnly()]

        return super().get_permissions()

    def post(self, request, slug):
        try:
            # author = Author.objects.get(slug=slug)
            review_data = request.data.get('review')
            
            # serializer_context = self.get_serializer_context()
            # serializer_context['author'] = author

            serializer = self.get_serializer(data=review_data) #, context=serializer_context)
            serializer.is_valid(raise_execption=True)
            self.perform_create(serializer)

            return Response({"review": serializer.data}, status = HTTP_200_OK)

        except Exception:
            return Response({
                "errors": {
                    "body": [
                        "review not happen"
                    ]
                }
            }, status = status.HTTP_404_NOT_FOUND)