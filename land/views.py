from django.shortcuts import render
from .serializers import PropertySerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .models import Property
from rest_framework import filters



class PropertyList(ListAPIView):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()
    search_fields = ['title', 'location']
    filter_backends = (filters.SearchFilter,)


class PropertyUpdate(RetrieveUpdateAPIView):
    serializer_class =PropertySerializer
    queryset = Property.objects.all()


class PropertyDelete(RetrieveDestroyAPIView):
    serializer_class =PropertySerializer
    queryset = Property.objects.all()
