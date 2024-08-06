"""
URL configuration for studentmanagementsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from app1.views import  * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name="home"),
    path("student/",add_sutdent,name="student"),
    path("editstudent/<id>/",edit_student,name= "editstudent"),
    path("deletestudent/<id>/",delete_student,name="delete_student"),



    path("book/",add_book,name="book"),
    path("editbook/<id>/",edit_book,name="edit_book"),
    path("deletebook/<id>/",delete_book,name="delete_book"),


    path("librarydata/",librarydata,name="library"),
    path("editlibrary/<id>/",edit_libarry,name="edit_library"),
    path("deletelibrary/<id>/",delete_library,name="delete_library"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
