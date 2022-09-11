from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# # Create your views here.


from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics,permissions



#To Read a book from db
@api_view(['GET'])
def Book(request):
    queryset=Books.objects.all()
    serializer=BookSerializer(queryset,many=True)
    return Response(serializer.data)

#To create new book in db
@api_view(['POST'])
def PostBook(request):
    queryset=Books.objects.all()
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


 #To update a book in db  
@api_view(['POST'])
def UpdateBook(request,id):
    queryset=Books.objects.get(id=id)
    serializer=BookSerializer(instance=queryset,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#to delete a book
@api_view(['DELETE'])
def DeleteBook(request,id):
    queryset=Books.objects.get(id=id)
    queryset.delete()
    return Response("Book is deleted")