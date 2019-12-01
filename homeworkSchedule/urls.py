"""homeworkSchedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from homeworkScheduleWeb.views import dashboard_view, class_View, assignments_view, assignment_view, delete_assignment, \
    comments_view, delete_comment, AddAssignment, UpdateAssignment
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    ##url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^api', include('homeworkScheduleWeb.urls')),
    url(r'^homePage/', login_required(dashboard_view)),
    url(r'^classes/', login_required(class_View)),
    url('^assignments/(?P<class_id>\d+)/$', login_required(assignments_view)),
    url('^assignment_preview/(?P<id>\d+)/$', login_required(assignment_view), name='previewAssignment'),
    url('^delete_assignment/(?P<pk>\d+)/(?P<class_id>\d+)/$', delete_assignment),
    url('^assignment_edit/(?P<id>\d+)/$', login_required(assignment_view)),
    url('^comments/', login_required(comments_view)),
    url('^delete_comment/(?P<pk>\d+)/$', delete_comment),
    url(r'^createAssignment/$', AddAssignment.as_view(), name='addAssignment'),
    url(r'^updateAssignment/(?P<pk>\d+)/$', UpdateAssignment.as_view(), name='updateAssignment'),
]
