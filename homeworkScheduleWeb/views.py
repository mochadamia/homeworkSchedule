from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Assignment, Comment, ClassName
from .serializers import AssignmentSerializer, CommentSerializer, ClassSerializer


def myView(request):
    ## return HttpResponse('hello world');
    return render(request, 'dashboard.html')


class AssignmentViewSet(generics.ListCreateAPIView):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        queryset = Assignment.objects.all().prefetch_related('comments')
        id = self.kwargs.get('pk', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class CommentViewSet(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        id = self.kwargs.get('pk', None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class ClassViewSet(generics.ListCreateAPIView):
    queryset = ClassName.objects.all()
    serializer_class = ClassSerializer