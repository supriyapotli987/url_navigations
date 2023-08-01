from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request,'contact.html')
def task(request):
    return render(request,'task.html')