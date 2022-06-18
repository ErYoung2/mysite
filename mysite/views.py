from django.http import HttpResponse

def demopage(request):
    return HttpResponse("This is a test page.")