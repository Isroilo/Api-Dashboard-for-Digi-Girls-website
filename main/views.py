from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def banner_view(request):
    banner = Banner.objects.filter(is_active=True)
    serializer = BannerSerializer(banner)
    return Response(serializer.data)
    return Response({'message':'None'})


@api_view(['GET'])
def about_info_view(request):
    about_info = About_Info.objects.last()
    serializer = About_ProjectSerializer(about_info)
    return Response(serializer.data)


@api_view(['GET'])
def about_project_view(request):
    about_project = About_Project.objects.filter(is_active=True).order_by('-id')
    serializer = About_ProjectSerializer(about_project,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def courses_info_view(request):
    courses_info = Courses_Info.objects.last()
    serializer = Courses_InfoSerializer(courses_info)
    return Response(serializer.data)


@api_view(['GET'])
def course_view(request):
    courses = Course.objects.filter(is_active=True).order_by('-id')
    serializer = CourseSerializer(courses,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_info_view(request):
    task_info = Task_info.objects.last()
    serializer = Task_infoSerializer(task_info)
    return Response(serializer.data)


@api_view(['GET'])
def task_view(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def register(request):
    name = request.POST.get('name')
    f_name = request.POST.get('f_name')
    birth = request.POST.get('birth')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    address = request.POST.get('address')
    try:
        new_register = Register.objects.create(
            name=name,
            f_name=f_name,
            birth=birth,
            phone=phone,
            email=email,
            address=address,
        )
        serializer = RegisterSerializer(new_register)
        return Response(serializer.data)
    except:
        return Response({"message" :"oldin bu raqam yoki emaildan foydalanilgan"})

@api_view(['GET'])
def result_info_view(request):
    result_info = Result_info.objects.last()
    serializer = Result_infoSerializer(result_info)
    return Response(serializer.data)


@api_view(['GET'])
def result_view(request):
    results = Result.objects.filter(is_active=True).order_by('-id')
    serializer = ResultSerializer(results,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def contact_view(request):
    contacts = Contact.objects.last()
    serializer = ContactSerializer(contacts)
    return Response(serializer.data)


@api_view(['GET'])
def info_view(request):
    infos = Info.objects.last()
    serializer = InfoSerializer(infos)
    return Response(serializer.data)

#
# import json
#
#product =  json.dumps(Prd.objects.all())