from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    return render(request,'result.html',{'result':val3})
# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def link(request):
    return render(request,'link.html')
    
