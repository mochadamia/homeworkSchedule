from django.urls import path

from . import views

urlpatterns = [
    path('/assignments/', views.Assignment.as_view()),
    path('/assignments/<int:pk>', views.Assignment.as_view()),
    path('/comments/', views.ListComment.as_view()),
    path('/comments/<int:pk>/', views.DetailComment.as_view()),
    path('/classes/', views.ListClass.as_view()),
]