from rest_framework import serializers
from .models import Book, School

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class SchoolSerializers(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'