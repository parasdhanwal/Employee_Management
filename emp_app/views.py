from django.shortcuts import render
from . models import Employee,Role,Department
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def add_emp(request):
     if request.method=='POST':
         first_name=request.POST['first_name']
         last_name=request.POST['last_name']
         salary=request.POST['salary']
         bonus=request.POST['bonus']
         phone=request.POST['first_name']
         dept=request.POST['dept']
         role=request.POST['role']

         new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
     else:
         return render(request,'add_emp.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
    'emps':emps
    }
    return render(request,'all_emp.html',context)

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')
