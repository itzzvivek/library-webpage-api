from rest_framework import serializers
from core.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title','subtitle','author','isbn')