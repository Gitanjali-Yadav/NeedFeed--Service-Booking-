# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service, ServiceCategory
from .serializers import ServiceSerializer, ServiceCategorySerializer  # Ensure this import is correct

class ServiceList(APIView):
    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceDetail(APIView):
    def get(self, request, pk):
        service = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(service)
        return Response(serializer.data)

class ServiceCategoryList(APIView):
    def get(self, request):
        categories = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer(categories, many=True)
        return Response(serializer.data)

class ServiceCategoryDetail(APIView):
    def get(self, request, pk):
        category = ServiceCategory.objects.get(pk=pk)
        serializer = ServiceCategorySerializer(category)
        return Response(serializer.data)