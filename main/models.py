from django.db import models
from phone_field import PhoneField


class Banner(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="banner/")
    info_uz = models.TextField(null=True,blank=True)
    info_ru = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=False)

class About_Info(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    text_uz = models.TextField(blank=True,null=True)
    text_ru = models.TextField(blank=True,null=True)

class About_Project(models.Model):
    photo = models.ImageField(upload_to="about_us/")
    info_uz = models.TextField()
    info_ru = models.TextField()
    is_active = models.BooleanField(default=False)

class Courses_Info(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    text_uz = models.TextField(blank=True,null=True)
    text_ru = models.TextField(blank=True,null=True)

class Course(models.Model):
    icon = models.ImageField(upload_to="course_icon/")
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)


class Task_info(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    text_uz = models.TextField(blank=True,null=True)
    text_ru = models.TextField(blank=True,null=True)

class Task(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)

class Result_info(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    text_uz = models.TextField(blank=True,null=True)
    text_ru = models.TextField(blank=True,null=True)

class Register(models.Model):
    name = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    birthday = models.DateField()
    phone = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


class Result(models.Model):
    icon = models.ImageField(upload_to="result_icon/")
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

class Info(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="about_us/")
    telegram = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)

class Contact(models.Model):
    internet = models.CharField(max_length=100)
    phone = PhoneField(help_text='Contact phone number')
    email = models.CharField(max_length=100)
    address_uz= models.CharField(max_length=255)
    address_ru = models.CharField(max_length=255)
    map_lot = models.CharField(max_length=100)
    map_long = models.CharField(max_length=100)













