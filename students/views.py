from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


@api_view(['GET'])
def studentlist(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def studentview(request, pk):
    students = Student.objects.get(studentId=pk)
    serializer = StudentSerializer(students, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def studentcreate(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def studentupdate(request, pk):
    students = Student.objects.get(studentId=pk)
    serializer = StudentSerializer(instance=students, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def studentdelete(request, pk):
    students = Student.objects.get(studentId=pk)
    students.delete()
    return Response("Successfully Deleted")




    



