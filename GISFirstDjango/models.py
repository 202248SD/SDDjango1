from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=1)


class Student(models.Model):
    name = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)
    grade = models.CharField(max_length=2)
    gmail = models.EmailField()


class Teacher(models.Model):
    name = models.OneToOneField(Person, null=True, on_delete=models.SET_NULL)
    subject = models.CharField(max_length=30)


class TeachingGroup(models.Model):
    teacher = models.OneToOneField(Teacher, null=True, on_delete=models.SET_NULL)
    students = models.ManyToManyField(Student, null=True)
