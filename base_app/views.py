from django.shortcuts import redirect, render
from django.http import HttpResponse
from base_app.forms import EmployeeForm
from base_app.models import Employee 
# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'base/index.html',{'form':form})  

def addnewuser(request): 
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass
    else:  
        form = EmployeeForm()  
    return render(request,'base/show.html',{'form':form})

def index(request):  
    employees = Employee.objects.all()

    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')   
            except:  
                pass
    else:  
        form = EmployeeForm()

    return render(request,"base/show.html",{'employees':employees, 'form':form})  
 
def updateUser(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
     


def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'base/edit.html', {'employee':employee})  
 
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'base/edit.html', {'employee': employee})  
     
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")