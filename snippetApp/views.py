from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication  
from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Snippet.objects.all()
        serializer = SnippetSerializer(queryset, many=True)
        return Response({'count': queryset.count(), 'snippets': serializer.data})

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        queryset = Snippet.objects.filter(tags__title=pk)
        serializer = SnippetSerializer(queryset, many=True)
        return Response(serializer.data)
