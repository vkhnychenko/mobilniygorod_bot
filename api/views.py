from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ManualItem, ManualCategory
from .serializers import ManualItemSerializer, ManualCategorySerializer
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet


class ManualCategoryView(ReadOnlyModelViewSet):
    queryset = ManualCategory.objects.filter(is_active=True)
    serializer_class = ManualCategorySerializer


class ManualItemView(ListAPIView):
    queryset = ManualItem.objects.all()
    serializer_class = ManualItemSerializer

    # def get_queryset(self):
    #     query = self.request.data.get("query")
    #     print('query: ', query)
    #     print('queryset', self)