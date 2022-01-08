from django.contrib import admin


from .models.students import Student


# Register your models here.

class AdminStudent(admin.ModelAdmin):
    list_display=['id',"first_name",'last_name','rool','city','marks','pass_date']

admin.site.register(Student,AdminStudent)
