from rest_framework import serializers
from .models import Book
import re
class BookSerialzer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields = ['id', 'title', 'author', 'isbn', 'published_year']

    def validate_isbn(self, value):
        if len(value)  != 13:
            raise serializers.ValidationError("ISBN should be 13 digits long.")
        return value
    def validate_published_year(self, value):
        if value < 1900 or value > 2024:
            raise serializers.ValidationError("Published year should be between 1900 and 2024.")
        return value
    def validate_title(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Title cannot be empty.")
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
       
        
        return value

    def validate_author(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Author cannot be empty.")
        if len(value) < 3:
            raise serializers.ValidationError("Author name must be at least 3 characters long.")
        
        if re.search(r'\d', value):
            raise serializers.ValidationError("Author name should not contain numbers.")
        
        return value
