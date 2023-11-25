from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

course_dictionary = {
    'python': 'Python Course Page', 
    'java': 'Java Course Page',
    'c++': 'C++ Course Page',
    'javascript': 'Javascript Course Page',
    'php': 'PHP Course Page',
}

def index(request):
    return HttpResponse("<em>This is my first app</em>")

def course(request, course_name):
    try:
        return HttpResponse(course_dictionary[course_name.lower()])
    except KeyError:
        return HttpResponseNotFound('<h1>Course not found!</h1>')
        #raise Http404('Course not found!')
    #return HttpResponse(course_dictionary.get(course_name.lower(), 'Course not found!'))

def multiply_view(request, num1, num2):
    return HttpResponse(f"{num1} * {num2} = {num1 * num2}")

def course_number_view(request, num1):
    course_list = list(course_dictionary.keys())
    try:
        course = course_list[num1]
        page_to_go = reverse('course', args=[course])
        return HttpResponseRedirect(page_to_go)
    except IndexError:
        return HttpResponseNotFound('<h1>Course not found!</h1>')
