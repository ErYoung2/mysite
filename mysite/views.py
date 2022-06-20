from django.shortcuts import render

def index(request):
    context = {}
    context["name"] = "Hello world"
    return render(request,"index.html",context)