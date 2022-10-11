from rest_framework import serializers
from library.models import Book, BookLike


class BookLikeSerializer(serializers.Serializer):
    class Meta:
        model = BookLike
        fields = ['date']


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=255)
    cover_url = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # book_likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    book_likes = BookLikeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.cover_url = validated_data.get('cover_url', instance.cover_url)

        instance.save()
        return instance

    class Meta:
        model = Book
        fields = ['__all__', 'book_likes']
