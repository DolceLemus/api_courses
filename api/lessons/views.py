from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.lessons.models import Lessons
from api.lessons.serializers import LessonsSerializer


class LessonsView(APIView):
    queryset = Lessons.objects.none()

    def get(self, request, id):
        lessons = Lessons.objects.get(pk=id)
        serializer = LessonsSerializer(lessons)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request,id):
        lessons = Lessons.objects.get(pk=id)
        serializer = LessonsSerializer(lessons, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            lessons = Lessons.objects.get(pk=id)
            lessons.delete()
        except:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class LessonsListView(APIView):
    queryset = Lessons.objects.none()

    def get(self, request):
        lessons = Lessons.objects.all()
        serializer = LessonsSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LessonsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)