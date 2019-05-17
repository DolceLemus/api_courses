from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.courses.models import Courses
from api.courses.serializers import CoursesSerializer


class CoursesView(APIView):
    queryset = Courses.objects.none()

    def get(self, request, id):
        courses = Courses.objects.get(pk=id)
        serializer = CoursesSerializer(courses)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id):
        courses = Courses.objects.get(pk=id)
        serializer = CoursesSerializer(courses, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            courses = Courses.objects.get(pk=id)
            courses.delete()
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class CoursesListView(APIView):
    queryset = Courses.objects.none()

    def get(self, request):
        courses = Courses.objects.all()
        serializer = CoursesSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)