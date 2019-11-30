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
from django.urls import path, include
from homeworkScheduleWeb.views import dashboard_view, class_View, assignments_view, assignment_view, delete_assignment, \
    comments_view, delete_comment

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api', include('homeworkScheduleWeb.urls')),
    url(r'^homePage/', dashboard_view),
    url(r'^classes/', class_View),
    url('^assignments/(?P<class_id>\d+)/$', assignments_view),
    url('^assignment_preview/(?P<id>\d+)/$', assignment_view),
    url('^delete_assignment/(?P<pk>\d+)/(?P<class_id>\d+)/$', delete_assignment),
    url('^comments/', comments_view),
    url('^delete_comment/(?P<pk>\d+)/$', delete_comment),
]
