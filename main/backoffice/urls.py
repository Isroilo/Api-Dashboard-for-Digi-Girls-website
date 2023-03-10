from django.urls import path ,include
from .views import *

urlpatterns = [
    path('excel/', include("excel_app.urls")),
    path("", home_view, name="dashboard"),
    path("sign-in/", signin_view, name="login_url"),
    path("log-out/", logout_view, name="logout_url"),
    path('user/update/', user_update, name='user_update_url'),
    path("banner/", banner_view, name="banner_url"),
    path("search/", search_view, name="search_name_url"),
    path("activate-banner/<int:pk>/", activate_banner, name="activate_banner_url"),
    path("delete-banner/<int:pk>/", delete_banner, name="delete_banner_url"),
    path("create-banner/", create_banner, name="create_banner_url"),
    path("update-banner/", update_banner, name="update_banner_url"),
    path("about-info/", about_info_view, name="about_info_url"),
    path("create-about-title/", create_about_title, name="create_about_title_url"),
    path("update-about-title/", update_about_title, name="update_about_title_url"),
    path("delete-about-title/<int:pk>/", delete_about_title, name="delete_about_title_url"),
    path("about-project/", about_project_view, name="about_project_url"),
    path("modal-about/<int:pk>/", modal_about, name="modal_about_url"),
    path("activate-project/<int:pk>/", activate_project, name="activate_project_url"),
    path("create-about-project/", create_about_project, name="create_infos_url"),
    path("update-about-project/", update_about_project, name="update_infos_url"),
    path("delete-about_-project/<int:pk>/", delete_about_project, name="delete_infos_url"),
    path("course-info/", course_info_view, name="course_info_url"),
    path("create-course-title/", create_course_title, name="create_course_title_url"),
    path("update-course-title/", update_course_title, name="update_course_title_url"),
    path("delete-course-title/<int:pk>/", delete_course_title, name="delete_course_title_url"),
    path("courses/", course_view, name="course_url"),
    path("modal-course/<int:pk>/", modal_course, name="modal_course_url"),
    path("activate-course/<int:pk>/", activate_course, name="activate_course_url"),
    path("create-course/", create_course, name="create_course_url"),
    path("update-course/", update_course, name="update_course_url"),
    path("delete-course/<int:pk>/", delete_course, name="delete_course_url"),
    path("result-info/", result_info_view, name="result_info_url"),
    path("create-result-title/", create_result_title, name="create_result_title_url"),
    path("update-result-title/", update_result_title, name="update_result_title_url"),
    path("delete-result-title/<int:pk>/", delete_result_title, name="delete_result_title_url"),
    path("result/", result_view, name="result_url"),
    path("modal-result/<int:pk>/", modal_result, name="modal_result_url"),
    path("activate-result/<int:pk>/", activate_result, name="activate_result_url"),
    path("create-result/", create_result, name="create_result_url"),
    path("update-result/", update_result, name="update_result_url"),
    path("delete-result/<int:pk>/", delete_result, name="delete_result_url"),
    path("tasks/", task_view, name="tasks_url"),
    path("create-task/", create_task, name="create_task_url"),
    path("update-task/", update_task, name="update_task_url"),
    path("delete-task/<int:pk>/", delete_task , name="delete_task_url"),
    path("task-info/", task_info_view, name="task_info_url"),
    path("create-task-title/", task_title_create, name="task_title_create_url"),
    path("update-task-title/", update_task_title, name="update_task_title_url"),
    path("delete-task-title/<int:pk>/", delete_task_title, name="delete_task_title_url"),
    path("infos/", infos_view, name="infos_url"),
    path("create-info/", create_info, name="create_info_url"),
    path("update-info/", update_info, name="update_info_url"),
    path("delete-info/<int:pk>/", delete_info, name="info_delete_url"),
    path("contact/", contact_view, name="contact_url"),
    path("create-contact/", create_contact, name="create_contact_url"),
    path("update-contact/", update_contact, name="update_contact_url"),
    path("delete-contact/<int:pk>/", delete_contact_view, name="delete_contact_url"),
    path("register/", register_view, name="register_url"),
]