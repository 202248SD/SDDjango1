from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=False, null=True)
    gender = models.CharField(max_length=1, null=True)


class Student(models.Model):
    name = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)
    grade = models.CharField(max_length=2)
    gmail = models.EmailField(null=True)


class Teacher(models.Model):
    name = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=30)


class TeachingGroup(models.Model):
    name = models.CharField(max_length=30, null=True)
    teacher = models.OneToOneField(Teacher, null=True, on_delete=models.SET_NULL)
    year_group = models.IntegerField(blank=False, null=True)
    students = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)



