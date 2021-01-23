from django.shortcuts import render, HttpResponse


def test(request):
    return HttpResponse("hi")

def second(request):
    return HttpResponse("test2 page")