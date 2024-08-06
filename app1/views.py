from django.shortcuts import render ,redirect
from django.http import HttpResponse,HttpResponseRedirect
from app1.forms import *
from app1.models import  *

# Create your views he



def home(request):
  return render(request,"app1/base.html")



# ========================================================
# student adding
# ======================================================

def add_sutdent(request):
  formemp=Studentform()
  if request.method=="GET":
    student_data=Student.objects.all()
    return render(request,"app1/student.html",context={"form":formemp,"students":student_data})
  elif request.method=="POST":
    form=Studentform(request.POST,request.FILES)
    if form.is_valid():
      form.save(commit=True)      
  return  redirect('student')


def delete_student(request,id): 
  student = Student.objects.get(id=id)
  print(student)
  student.delete()
  return  redirect('student')

def edit_student(request,id):
  if request.method=="GET":
    stud = Student.objects.get(id=id)
    form = Studentform(instance= stud)
    return render(request,"app1/student.html",context={"form":form})
  elif request.method=="POST":
    stud = Student.objects.get(id=id)
    form  = Studentform(request.POST,request.FILES,instance=stud)
    if form.is_valid():
      form.save()
      return redirect('student')
    




   

# =============================================================
#  bOOK DATA
# ================================================================
      
      
def add_book(request):
  formbook = Booksform()
  if request.method=="GET":
    book_data=Books.objects.all()
    return render(request,'app1/books.html',{'form':formbook,'books':book_data})
  elif request.method=="POST":
    formbook=Booksform(request.POST)
    if formbook.is_valid():
      formbook.save(commit=True)
  return redirect('book')


def delete_book(request,id): 
  student = Books.objects.get(id=id)
  print(student)
  student.delete()
  return  redirect('book')



def edit_book(request,id):
  if request.method=="GET":
    stud = Books.objects.get(id=id)
    form = Booksform(instance= stud)
    return render(request,"app1/books.html",context={"form":form})
  elif request.method=="POST":
    stud = Books.objects.get(id=id)
    form  = Booksform(request.POST,instance= stud)
    if form.is_valid():
      form.save()
      return redirect('book')
    



# ============================================================
# librarydata
# ++++++++++++++++++++============================


     
def librarydata(request): 
  formlibrary = Libraryform()
  if request.method=="GET": 
    library_data=Library.objects.all()
    return render(request,'app1/library.html',{'form':formlibrary,"library_data":library_data})
  elif request.method=="POST":
    formlibrary=Libraryform(request.POST)
    if formlibrary.is_valid():
      formlibrary.save(commit=True)
  return  redirect('library')


def delete_library(request,id): 
  student = Library.objects.get(id=id)
  student.delete()
  return  redirect('library')

def edit_libarry(request,id):
  if request.method=="GET":
    stud =  Library.objects.get(id=id)
    form = Libraryform(instance= stud)
    return render(request,"app1/books.html",context={"form":form})
  elif request.method=="POST":
    stud = Library.objects.get(id=id)
    form  = Libraryform(request.POST,instance= stud)
    if form.is_valid():
      form.save()
  return redirect('library')

