from django.shortcuts import render
from rest_framework import generics

from bt.models import Worm
from bt.serializers import WormSerializer


class WormList(generics.ListCreateAPIView):
    queryset = Worm.objects.all()
    serializer_class = WormSerializer


class WormDetail(generics.RetrieveUpdateAPIView):
    queryset = Worm.objects.all()
    serializer_class = WormSerializer