from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from homeworkScheduleWeb.forms import PostComment
from .models import Assignment, Comment, ClassName
from .serializers import AssignmentSerializer, CommentSerializer, ClassSerializer


def dashboard_view(request):
    return render(request, 'dashboard.html')


def class_View(request):
    class_name = list(ClassName.objects.all())
    data = {'class_name': class_name}
    return render(request, 'classes.html', data)


def assignments_view(request, class_id):
    assignments = list(Assignment.objects.filter(class_id=class_id))
    data = {'assignments': assignments}
    return render(request, 'assignments.html', data)


def assignment_view(request, id):
    if request.method == 'POST':
        form = PostComment(request.POST)
        assignment = get_object_or_404(Assignment, pk=id)
        user = get_object_or_404(User, pk=1)

        if form.is_valid():
            comment = form.save(commit=False)
            cd = form.cleaned_data
            comment.content = cd['content']
            comment.assignment_id = assignment
            comment.status = 1
            comment.user_id = user
            comment.save()
    else:
        form = PostComment()
    assignment = Assignment.objects.get(id=id)
    comments = list(Comment.objects.filter(assignment_id=id))

    data = {'assignment': assignment, 'comments': comments, 'form': form}
    return render(request, 'preview_assignment.html', data)


class AssignmentViewSet(generics.ListCreateAPIView):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        queryset = Assignment.objects.all().prefetch_related('comments')
        id = self.kwargs.get('pk', None)
        if id is not None:
            queryset = queryset.filter(id=id)

        class_id = self.request.query_params.get('class_id', None)
        if class_id is not None:
            queryset = queryset.filter(class_id=class_id)
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