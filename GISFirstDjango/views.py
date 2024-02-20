from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Billy'
    people = Person.objects.all()
    debug_people = list(people)
    return render(request, "splash.html", {'name': name})


def display_list(request):
    my_list = ['item1', 'item2', 'item3']  # Replace this with your list of values
    return render(request, 'display_list.html', {'my_list': my_list})

def display_persons(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})



