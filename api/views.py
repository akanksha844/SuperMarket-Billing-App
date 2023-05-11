from django.shortcuts import render


# Create your views here
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend



class ItemView(viewsets.ModelVieeSet):
    http_method_names = ['get', 'post', 'put']
    queryset= Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('name', 'category', 'subcategory')
    
    def put(self, request):
        return self.semi_update(request)
    
    
    def semi_update(self, request) :
        instance = self.queryset.get(pk = request.GET['id'])
        serializer = self.serializer_class(instance, data = request.data, partial =True)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data)
            