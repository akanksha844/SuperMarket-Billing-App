# from django.db.models import fields
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta :
        model = Item
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')