from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, status

from .serializers import TrashPostSerializer
from .models import TrashPost

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TrashPostView(generics.CreateAPIView):
    queryset = TrashPost.objects.all()
    serializer_class = TrashPostSerializer

class TrashPostList(generics.ListAPIView):
    queryset = TrashPost.objects.all()
    serializer_class = TrashPostSerializer