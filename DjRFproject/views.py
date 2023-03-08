from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from DjRFapp.serializers import StudentSerializer
from DjRFapp.models import Student

class TestView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        student1 = qs.first()
        serializer = StudentSerializer(student1)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)