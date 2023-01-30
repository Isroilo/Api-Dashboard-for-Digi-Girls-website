from django.urls import path, include
from .views import *

urlpatterns = [
    path("banner/", banner_view),
    path("about_info/", about_info_view),
    path("about/", about_project_view),
    path("courses_info/", courses_info_view),
    path("course/", course_view),
    path("task_info/", task_info_view),
    path("task/", task_view),
    path("register/", register),
    path("result_info/", result_info_view),
    path("result/", result_view),
    path("contact/", contact_view),
    path("info/", info_view),
]
