from django import forms
from app1.models import *


# form for the Student data
class Studentform(forms.ModelForm):
  class Meta:
    model= Student
    fields= '__all__'

#form For the Booksdata
class Booksform(forms.ModelForm):
  class Meta:
    model = Books
    fields= '__all__'
    widgets ={
      "year":forms.DateInput(attrs={"type":'date'})
    }

#  book  avilability data
class Libraryform(forms.ModelForm):
  class Meta:
    model=Library
    fields ="__all__"
    widgets={
      "starteddate":forms.DateInput(attrs={"type":'date'}),
      "endedate": forms.DateInput(attrs={"type":"date"}),
    }

