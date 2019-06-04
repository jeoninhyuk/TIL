from django.shortcuts import render

def index(request):
    return render(request, 'utilities/index.html')

def imagepick(request):
    return render(request, 'utilities/imagepick.html')