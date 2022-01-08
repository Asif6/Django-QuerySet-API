from django import views
from django.shortcuts import render
from django.views import View
from .models.students import Student

# Create your views here.


class Index(views.View):
    def get(self,request):

        all_student= Student.objects.all()

        return render(request,'index.html', {'student':all_student})