from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Ticket, City, Department, Area, Region
from .serializers import TicketSerializer, CitySerializer, DepartmentSerializer, AreaSerializer, RegionSerializer


class TicketAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        ticket = Ticket.objects.filter(owner=request.user)
        serializer = TicketSerializer(ticket, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request):
        ticket_id = request.data.get('id')
        try:
            ticket = Ticket.objects.get(id=ticket_id, owner=request.user)
        except Ticket.DoesNotExist:
            return Response({'error': 'Билет не найден'}, status=404)

        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk, owner=request.user)
        except Ticket.DoesNotExist:
            return Response({'error': 'Билет не найден'}, status=404)

        ticket.delete()
        return Response(status=204)
    
class RegionAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        area = Area.objects.all()
        serializer = RegionSerializer(area, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            region = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return Response({'error': 'Область не найдена'}, status=404)

        serializer = RegionSerializer(region, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            region = Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            return Response({'error': 'Область не найдена'}, status=404)

        region.delete()
        return Response(status=204)

class AreaAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        area = Area.objects.all()
        serializer = AreaSerializer(area, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            area = Area.objects.get(pk=pk)
        except Area.DoesNotExist:
            return Response({'error': 'Район не найден'}, status=404)

        serializer = AreaSerializer(area, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            area = Area.objects.get(pk=pk)
        except Area.DoesNotExist:
            return Response({'error': 'Район не найден'}, status=404)

        area.delete()
        return Response(status=204)

class CityAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        city = City.objects.all()
        serializer = CitySerializer(city, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            city = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response({'error': 'Город не найден'}, status=404)

        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            city = City.objects.get(pk=pk)
        except City.DoesNotExist:
            return Response({'error': 'Город не найден'}, status=404)

        city.delete()
        return Response(status=204)
    

class DepartmentAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        department = Department.objects.all()
        serializer = DepartmentSerializer(department, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response({'error': 'Отделение не найдено'}, status=404)

        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        try:
            department = Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return Response({'error': 'Отделение не найдено'}, status=404)

        department.delete()
        return Response(status=204)
