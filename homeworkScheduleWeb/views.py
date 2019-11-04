from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Assignment, Comment, Class
from .serializers import AssignmentSerializer, CommentSerializer, ClassSerializer


def myView(request):
    ## return HttpResponse('hello world');
    return render(request, 'dashboard.html')


class Assignment(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ListClass(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer