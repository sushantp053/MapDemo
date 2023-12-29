from django.shortcuts import render
from api.serializers import NatoshiSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from home.models import Natoshi

class NatoshiViewSet(viewsets.ModelViewSet):
    queryset = Natoshi.objects.all()
    serializer_class = NatoshiSerializer


class NatoshiViewSet1(APIView):
    
    def get(self, request, format=None):
        natoshi = Natoshi.objects.all()
        serializer = NatoshiSerializer(natoshi, many=True)
        return Response(serializer.data)
