from django.shortcuts import render, HttpResponse


def test(request):
    return render(request, "index.html")