from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('/assignments/', views.AssignmentViewSet.as_view()),
    path('/assignments/<int:pk>', views.AssignmentViewSet.as_view()),
    path('/comments/', views.CommentViewSet.as_view()),
    path('/comments/<int:pk>/', views.AssignmentViewSet.as_view()),
    path('/classes/', views.ClassViewSet.as_view()),
]