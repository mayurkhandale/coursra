from django.shortcuts import render
from django.views.generic import View

from .models import StudentModal
from .form import StudentForm
# Create your views here.

class StudentView(View):
    def get(self,request):
        data=StudentForm()
        return render(request,'main/index.html',{"data":data})
    def post(self,request):
        data=StudentForm(request.POST)
        if data.is_valid():
            data.save()
            message="Succesfully Save Data"
            return render(request,"main/index.html",{"ms":message,"data":StudentForm})
        else:
            return render(request,"main/index.html",{"error":"Something Wrong","data":StudentForm})


def About(request):
    return render(request,"main/about.html")

def course(request):
    return render(request,"main/course.html")

def instructor(request):
    return render(request,"main/instructer.html")

def  blog(request):
    return render(request,"main/blog.html")

def contact(request):
    return  render(request,"main/contact.html")

def mycourses(request):
    return render(request,"main/mycourses.html")

class Loginpage(View):
    def get(self,request):
        return render(request,"main/loginpage.html")
    def post(self,request):
       name=request.POST['t1']
       passw=request.POST['t2']
       try:
           student=StudentModal.objects.get(s_f_name=name,password=passw)
           return render(request,'main/welcome.html',{"student":student})
       except StudentModal.DoesNotExist:
           error="Username & password Does Not Exist"
           return render(request,'main/loginpage.html',{"eror":error})

def Itcourses(request):
    return render(request,"main/itcourse.html")

