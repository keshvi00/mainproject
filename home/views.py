from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from home.models import Admin
from .forms import tasksentry

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def kanban(request):
    return render(request, 'kanban.html')

def home(request):
    return render(request,'home.html')

def room(request):
    return render(request,'room.html')

def tasks(request):
    if request.method =='POST':
        fm=tasksentry(request.POST)
        if fm.is_valid():
           fm.save()
    else:
        fm=tasksentry()
    return render(request,'templates/tasks.html', {'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=Admin.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def dashboard(request):
    data = {
        'labels': ['January', 'February', 'March', 'April', 'May'],
        'values': [10, 20, 15, 25, 30]  # Sample data
    }
    return render(request, 'dashboard.html', {'data': data})
