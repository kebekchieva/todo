from django.shortcuts import render, HttpResponse


def test(request):
    return HttpResponse("hi")

def second(request):
    return HttpResponse("test2 page")

def hw3(request):
    return HttpResponse("This is page test3")