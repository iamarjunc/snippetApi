from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']

class SnippetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ['title', 'content', 'created_at', 'created_by', 'tags']

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        snippet = Snippet.objects.create(**validated_data)
        for tag in tags:
            t, created = Tag.objects.get_or_create(title=tag['title'])
            snippet.tags.add(t)
        return snippet
