from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("hello")


def go (request):
    return render (request, "index.html")