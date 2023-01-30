from django.shortcuts import render, redirect
from main.models import *
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.db.models import Count
from django.db.models.functions import ExtractDay, ExtractMonth
import calendar



#  start dashboard -->
@login_required(login_url='login_url')
def home_view(request):
    all_register = Register.objects.all().order_by('id').count()
    day = datetime.today() - timedelta(days=1)
    month = datetime.today() - timedelta(days=30)
    today = Register.objects.filter(created__gte=day).count()
    months = Register.objects.filter(created__gte=month).count()
    qs = Register.objects.filter(
        created__gte=month
    ).annotate(
        day=ExtractDay("created"),
        mon=ExtractMonth('created'),
    ).values(
        'day', 'mon'
    ).annotate(
        n=Count('pk')
    ).order_by('mon')
    mon_list = []
    for i in qs:
        i['mon'] = (calendar.month_abbr[i['mon']])
        if len(mon_list) >= 30:
            del mon_list[0]
            mon_list.append(i)
        else:
            mon_list.append(i)
    context = {
       "all_register":all_register,
       "today":today,
       "month":months,
        "qs": mon_list,
    }
    return render(request, 'dashboard.html',context)
# and dashboard -->

# start auth -->
@login_required(login_url='login_url')
def search_view(request):
    if request.method == "POST":
        search = request.POST['search']
        search = Register.objects.filter(name__icontains=search)
        context = {
            'search':search
        }
        return render(request,'search.html',context)



def user_update(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST['username']
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        user.username = username
        if password is not None:
            if password == password_confirm:
                user.set_password(password)
            else:
                user.save()
        user.save()
        return redirect('user_update_url')
    context = {
        'user': request.user
    }
    return render(request, 'user-update.html' , context)


def signin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request,usr)
            return redirect('dashboard')
    return render(request, 'log-in.html')


@login_required(login_url='login_url')
def logout_view(request):
    logout(request)
    return redirect('dashboard')
# and auth -->

#  start banner -->
@login_required(login_url='login_url')
def banner_view(request):
    banners = Banner.objects.filter(is_active=True).order_by('-id')
    s_list = []
    for i in banners:
        s_list.append(i)
    context = {
        "banners":Banner.objects.all().order_by('-id'),
        "active_banners" : Banner.objects.filter(is_active=True).order_by('-id'),
        's_num' : len(s_list),
    }
    return render(request, 'banners.html', context)

@login_required(login_url='login_url')
def activate_banner(request,pk):
    banner = Banner.objects.get(id=pk)
    banners = Banner.objects.all()
    for i in banners:
        if i.is_active == True:
            i.is_active = False
            i.save()
        else:
            pass
    if banner.is_active == True:
        banner.is_active = False
        banner.save()
    else:
        banner.is_active = True
        banner.save()
    return redirect('banner_url')


@login_required(login_url='login_url')
def create_banner(request):
    if request.method == "POST":
        title_uz = request.POST.get("title_uz")
        title_ru = request.POST.get("title_ru")
        photo = request.FILES.get("photo")
        info_uz = request.POST.get("info_uz")
        info_ru = request.POST.get("info_ru")
        Banner.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            photo=photo,
            info_uz=info_uz,
            info_ru=info_ru,
        )
        return redirect("banner_url")
    return redirect("banner_url")


@login_required(login_url='login_url')
def update_banner(request):
    if request.method == 'POST':
        modal_id = request.POST['modal_id']
        banner = Banner.objects.get(pk=modal_id)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        info_uz = request.POST['info_uz']
        info_ru = request.POST['info_ru']
        photo = request.FILES.get('photo')
        banner.title_uz = title_uz
        banner.title_ru = title_ru
        banner.info_uz = info_uz
        banner.info_ru = info_ru
        if photo is not None:
            banner.photo = photo
        else:
            pass
        banner.save()
        return redirect('banner_url')
    context = {
        "banner": banner,
    }
    return render(request, 'update-banner.html', context)

@login_required(login_url='login_url')
def delete_banner(request, pk):
    banner = Banner.objects.get(pk=pk)
    banner.delete()
    return redirect('banner_url')
# and banner -->

# start about -->
@login_required(login_url='login_url')
def about_info_view(request):
    context = {
        "about_title": About_Info.objects.all().order_by('-id'),
    }
    return render(request,'about-info.html', context)


@login_required(login_url='login_url')
def create_about_title(request):
    if request.method == "POST":
        title_uz = request.POST.get("title_uz")
        title_ru = request.POST.get("title_ru")
        text_uz = request.POST.get("text_uz")
        text_ru = request.POST.get("text_ru")
        About_Info.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect("about_info_url")
    return redirect("about_info_url")


@login_required(login_url='login_url')
def update_about_title(request):
    if request.method == 'POST':
        modal_id = request.POST["modal_id"]
        about_title = About_Info.objects.get(pk=modal_id)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        text_uz = request.POST['text_uz']
        text_ru = request.POST['text_ru']
        about_title.title_uz = title_uz
        about_title.title_ru = title_ru
        about_title.text_uz = text_uz
        about_title.text_ru = text_ru
        about_title.save()
        return redirect('about_info_url')
    return redirect('about_info_url')


@login_required(login_url='login_url')
def delete_about_title(request, pk):
    about_title = About_Info.objects.get(pk=pk)
    about_title.delete()
    return redirect('about_info_url')


@login_required(login_url='login_url')
def about_project_view(request):
    projects = About_Project.objects.filter(is_active=True).order_by('-id')
    s_list = []
    for i in projects:
        s_list.append(i)
    context = {
        "projects" : About_Project.objects.all().order_by('-id'),
        "active_projects" : About_Project.objects.filter(is_active=True).order_by('-id'),
        's_num' : len(s_list),
    }
    return render(request, 'about-project.html', context)


@login_required(login_url='login_url')
def modal_about(request, pk):
    if request.method == "POST":
        modal_1 = request.POST["modal_id"]
        modal_project = About_Project.objects.get(id=modal_1)
        project = About_Project.objects.get(id=pk)
        project.is_active = True
        project.save()
        modal_project.is_active = False
        modal_project.save()
    return redirect('about_project_url')


@login_required(login_url='login_url')
def activate_project(request,pk):
    project = About_Project.objects.get(id=pk)
    if project.is_active == True:
        project.is_active = False
        project.save()
    else:
        project.is_active = True
        project.save()
    return redirect('about_project_url')


@login_required(login_url='login_url')
def create_about_project(request):
    if request.method == "POST":
        print("2222")
        photo = request.FILES["photo"]
        info_uz = request.POST["info_uz"]
        info_ru = request.POST["info_ru"]
        About_Project.objects.create(
            photo=photo,
            info_uz=info_uz,
            info_ru=info_ru,
        )
        return redirect("about_project_url")
    return redirect("about_project_url")


@login_required(login_url='login_url')
def update_about_project(request):
    if request.method == 'POST':
        modal_id = request.POST['modal_id']
        project = About_Project.objects.get(pk=modal_id)
        info_uz = request.POST['info_uz']
        info_ru = request.POST['info_ru']
        photo = request.FILES.get('photo')
        project.info_uz = info_uz
        project.info_ru = info_ru
        if photo is not None:
            project.photo = photo
        else:
            pass
        project.save()
        return redirect('about_project_url')
    return redirect('about_project_url')


@login_required(login_url='login_url')
def delete_about_project(request, pk):
    project = About_Project.objects.get(pk=pk)
    project.delete()
    return redirect('about_project_url')
#  and about -->

#  start course -->
@login_required(login_url='login_url')
def course_info_view(request):
    context = {
        "course_title": Courses_Info.objects.all().order_by('-id'),
    }
    return render(request, 'course-info.html', context)

@login_required(login_url='login_url')
def create_course_title(request):
    if request.method == 'POST':
        title_uz = request.POST["title_uz"]
        title_ru = request.POST["title_ru"]
        text_uz = request.POST["text_uz"]
        text_ru = request.POST["text_ru"]
        Courses_Info.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect("course_info_url")
    return redirect("course_info_url")


@login_required(login_url='login_url')
def update_course_title(request):
    if request.method == 'POST':
        modal_id = request.POST["modal_id"]
        course_title = Courses_Info.objects.get(pk=modal_id)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        text_uz = request.POST['text_uz']
        text_ru = request.POST['text_ru']
        course_title.title_uz = title_uz
        course_title.title_ru = title_ru
        course_title.text_uz = text_uz
        course_title.text_ru = text_ru
        course_title.save()
        return redirect("course_info_url")
    return redirect("course_info_url")


@login_required(login_url='login_url')
def delete_course_title(request, pk):
    course_title = Courses_Info.objects.get(pk=pk)
    course_title.delete()
    return redirect('course_info_url')


@login_required(login_url='login_url')
def course_view(request):
    active_courses = Course.objects.filter(is_active=True).order_by('-id')
    c_list = []
    for i in active_courses:
        c_list.append(i)
    context = {
        "courses" : Course.objects.all().order_by('-id'),
        "active_courses" : Course.objects.filter(is_active=True).order_by('-id'),
        'c_num' : len(c_list),
    }
    return render(request, 'courses.html', context)


@login_required(login_url='login_url')
def modal_course(request, pk):
    if request.method == "POST":
        modal_1 = request.POST["modal_id"]
        modal_course = Course.objects.get(id=modal_1)
        course = Course.objects.get(id=pk)
        course.is_active = True
        course.save()
        modal_course.is_active = False
        modal_course.save()
    return redirect('course_url')


@login_required(login_url='login_url')
def activate_course(request,pk):
    course = Course.objects.get(id=pk)
    if course.is_active == True:
        course.is_active = False
        course.save()
    else:
        course.is_active = True
        course.save()
    return redirect('course_url')


@login_required(login_url='login_url')
def create_course(request):
    if request.method == "POST":
        icon = request.FILES["icon"]
        name_uz = request.POST["name_uz"]
        name_ru = request.POST["name_ru"]
        Course.objects.create(
            icon=icon,
            name_uz=name_uz,
            name_ru=name_ru,
        )
        return redirect("course_url")
    return redirect("course_url")


@login_required(login_url='login_url')
def update_course(request):
    if request.method == 'POST':
        modal_id = request.POST['modal_id']
        course = Course.objects.get(pk=modal_id)
        name_uz = request.POST['name_uz']
        name_ru = request.POST['name_ru']
        icon = request.FILES.get('icon')
        course.name_uz = name_uz
        course.name_ru = name_ru
        if icon is not None:
            course.icon = icon
        course.save()
        return redirect('course_url')
    return redirect('course_url')


@login_required(login_url='login_url')
def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('course_url')
#   and course -->

#  start result -->
def result_info_view(request):
    context = {
        "result_title": Result_info.objects.all().order_by('-id'),
    }
    return render(request, 'result-info.html', context)


@login_required(login_url='login_url')
def create_result_title(request):
    if request.method == 'POST':
        title_uz = request.POST["title_uz"]
        title_ru = request.POST["title_ru"]
        text_uz = request.POST["text_uz"]
        text_ru = request.POST["text_ru"]
        Result_info.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect("result_info_url")
    return redirect("result_info_url")


@login_required(login_url='login_url')
def update_result_title(request):
    if request.method == 'POST':
        modal_id = request.POST["modal_id"]
        result_title = Result_info.objects.get(pk=modal_id)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        text_uz = request.POST['text_uz']
        text_ru = request.POST['text_ru']
        result_title.title_uz = title_uz
        result_title.title_ru = title_ru
        result_title.text_uz = text_uz
        result_title.text_ru = text_ru
        result_title.save()
        return redirect("result_info_url")
    return redirect("result_info_url")


@login_required(login_url='login_url')
def delete_result_title(request, pk):
    result_title = Result_info.objects.get(pk=pk)
    result_title.delete()
    return redirect('result_info_url')


@login_required(login_url='login_url')
def result_view(request):
    active_result = Result.objects.filter(is_active=True).order_by('-id')
    r_list = []
    for i in active_result:
        r_list.append(i)
    context = {
        "results" : Result.objects.all().order_by('-id'),
        "active_results" : Result.objects.filter(is_active=True).order_by('-id'),
        'r_num' : len(r_list),
    }
    return render(request, 'results.html', context)


@login_required(login_url='login_url')
def modal_result(request, pk):
    if request.method == "POST":
        modal_1 = request.POST["modal_id"]
        modal_result = Result.objects.get(id=modal_1)
        result = Result.objects.get(id=pk)
        result.is_active = True
        result.save()
        modal_result.is_active = False
        modal_result.save()
    return redirect('result_url')


@login_required(login_url='login_url')
def activate_result(request,pk):
    result = Result.objects.get(id=pk)
    if result.is_active == True:
        result.is_active = False
        result.save()
    else:
        result.is_active = True
        result.save()
    return redirect('result_url')


@login_required(login_url='login_url')
def create_result(request):
    if request.method == "POST":
        icon = request.FILES["icon"]
        title_uz = request.POST["title_uz"]
        title_ru = request.POST["title_ru"]
        Result.objects.create(
            icon=icon,
            title_uz=title_uz,
            title_ru=title_ru,
        )
        return redirect("result_url")
    return redirect("result_url")

@login_required(login_url='login_url')
def update_result(request):
    if request.method == 'POST':
        modal_id = request.POST['modal_id']
        result = Result.objects.get(pk=modal_id)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        icon = request.FILES.get('icon')
        result.title_uz = title_uz
        result.title_ru = title_ru
        if icon is not None:
            result.icon = icon
        result.save()
        return redirect('result_url')
    return redirect('result_url')


@login_required(login_url='login_url')
def delete_result(request, pk):
    result = Result.objects.get(pk=pk)
    result.delete()
    return redirect('result_url')

# and rusult -->

#  start task -->
@login_required(login_url='login_url')
def task_info_view(request):
    context = {
        "task_title": Task_info.objects.all().order_by('-id'),
    }
    return render(request, 'task-title.html', context)


@login_required(login_url='login_url')
def task_title_create(request):
    if request.method == 'POST':
        title_uz = request.POST["title_uz"]
        title_ru = request.POST["title_ru"]
        text_uz = request.POST["text_uz"]
        text_ru = request.POST["text_ru"]
        Task_info.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
            text_uz=text_uz,
            text_ru=text_ru,
        )
        return redirect("task_info_url")
    return redirect("task_info_url")


@login_required(login_url='login_url')
def update_task_title(request):
    if request.method == 'POST':
        modal_id = request.POST["modal_id"]
        task_title = Task_info.objects.get(pk=modal_id)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        text_uz = request.POST['text_uz']
        text_ru = request.POST['text_ru']
        task_title.title_uz = title_uz
        task_title.title_ru = title_ru
        task_title.text_uz = text_uz
        task_title.text_ru = text_ru
        task_title.save()
        return redirect("task_info_url")
    return redirect("task_info_url")


@login_required(login_url='login_url')
def delete_task_title(request, pk):
    task_title = Task_info.objects.get(pk=pk)
    task_title.delete()
    return redirect('task_info_url')


@login_required(login_url='login_url')
def task_view(request):
    tasks = Task.objects.all().order_by('-id')
    t_list = []
    for i in tasks:
        t_list.append(i)
    context = {
        "tasks": Task.objects.all().order_by('-id'),
        't_num': len(t_list),
    }
    return render(request, 'tasks.html',context)


@login_required(login_url='login_url')
def create_task(request):
    if request.method == "POST":
        title_uz = request.POST["title_uz"]
        title_ru = request.POST["title_ru"]
        Task.objects.create(
            title_uz=title_uz,
            title_ru=title_ru,
        )
        return redirect("tasks_url")
    return redirect("tasks_url")


@login_required(login_url='login_url')
def update_task(request):
    if request.method == 'POST':
        modal_id = request.POST['modal_id']
        task = Task.objects.get(pk=modal_id)
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        task.title_uz = title_uz
        task.title_ru = title_ru
        task.save()
        return redirect('tasks_url')
    return redirect('tasks_url')


@login_required(login_url='login_url')
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('tasks_url')

# and task -->
# start info -->
@login_required(login_url='login_url')
def infos_view(request):
    context = {
        "info":Info.objects.last(),
    }
    return render(request, 'info.html', context)


@login_required(login_url='login_url')
def create_info(request):
    if request.method == "POST":
        name = request.POST.get("name")
        telegram = request.POST.get("telegram")
        instagram = request.POST.get("instagram")
        youtube = request.POST.get("youtube")
        facebook = request.POST.get("facebook")
        icon = request.FILES.get("icon")
        Info.objects.create(
            name=name,
            telegram=telegram,
            instagram=instagram,
            youtube=youtube,
            facebook=facebook,
            icon=icon,
        )
        return redirect("infos_url")
    return redirect("infos_url")


@login_required(login_url='login_url')
def update_info(request):
    if request.method == 'POST':
        modal_id = request.POST['modal_id']
        info = Info.objects.get(pk=modal_id)
        telegram = request.POST['telegram']
        instagram = request.POST['instagram']
        youtube = request.POST['youtube']
        facebook = request.POST['facebook']
        name = request.POST['name']
        icon = request.FILES.get('icon')
        info.telegram = telegram
        info.instagram = instagram
        info.youtube = youtube
        info.facebook = facebook
        info.name = name
        if icon is not None:
            info.icon = icon
        info.save()
        return redirect('infos_url')
    return redirect('infos_url')


@login_required(login_url='login_url')
def delete_info(request,pk):
    info = Info.objects.get(pk=pk)
    info.delete()
    return redirect('infos_url')
#  and info -->

# start contact -->
@login_required(login_url='login_url')
def contact_view(request):
    context = {
        "contact":Contact.objects.last(),
    }
    return render(request, 'contact.html', context)


@login_required(login_url='login_url')
def create_contact(request):
    if request.method == "POST":
        address_uz = request.POST["address_uz"]
        address_ru = request.POST["address_ru"]
        phone = request.POST["phone"]
        map_lot = request.POST["map_lot"]
        map_long = request.POST["map_long"]
        internet = request.POST["internet"]
        email = request.POST["email"]
        Contact.objects.create(
            address_uz = address_uz,
            address_ru = address_ru,
            phone = phone,
            map_lot = map_lot,
            map_long = map_long,
            internet = internet,
            email = email,
        )
        return redirect("contact_url")
    return redirect("contact_url")


@login_required(login_url='login_url')
def update_contact(request):
    if request.method == 'POST':
        modal_id = request.POST['modal_id']
        contact = Contact.objects.get(pk=modal_id)
        address_uz = request.POST['address_uz']
        address_ru = request.POST['address_ru']
        internet = request.POST['internet']
        phone = request.POST['phone']
        map_lot = request.POST['map_lot']
        map_long = request.POST['map_long']
        email = request.POST['email']
        contact.address_uz = address_uz
        contact.address_ru = address_ru
        contact.internet = internet
        contact.phone = phone
        contact.map_lot = map_lot
        contact.map_long = map_long
        contact.email = email
        contact.save()
        return redirect('contact_url')
    return redirect('contact_url')


@login_required(login_url='login_url')
def delete_contact_view(request,pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('contact_url')

#  and contact --->

#  start register -->
def PagenatorPage(List, num ,request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


@login_required(login_url='login_url')
def register_view(request):
    users = Register.objects.all().order_by('-id')
    context = {
        "users": PagenatorPage(users, 5, request)
    }
    return render(request, 'register.html',context)





