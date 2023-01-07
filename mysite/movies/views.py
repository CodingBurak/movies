from django.shortcuts import render
from rest_framework import viewsets
from .serializiers import MovieSerializer
from .models import MovieData

# Create your views here.


class MovieViewSet(viewsets.ModelViewSet):
  queryset = MovieData.objects.all()
  serializer_class = MovieSerializer
  
  
class ActionViewSet(viewsets.ModelViewSet):
  queryset = MovieData.objects.filter(category="action")
  serializer_class = MovieSerializer
  
class DramaViewSet(viewsets.ModelViewSet):
  queryset = MovieData.objects.filter(category="drama")
  serializer_class = MovieSerializer