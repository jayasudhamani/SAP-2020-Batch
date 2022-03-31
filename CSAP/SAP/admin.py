from django.contrib import admin
from .models import Student
from django.urls import path, reverse
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Register your models here.

class CsvImportForm(forms.Form):
    csv_upload=forms.FileField()

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=("studentname","coursename","courseid","semester","semester_mark","semester_attendance","status")
    list_filter=("status","courseid","semester",)

    def get_urls(self):
        urls=super().get_urls()
        new_urls=[path('upload-csv/', self.upload_csv),]
        return new_urls+urls
    
    def upload_csv(self, request):
        if request.method=="POST":
            csv_file=request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request,"Invalid File.")
                return HttpResponseRedirect(request.path_info)

            file_data=csv_file.read().decode("utf-8")
            csv_data=file_data.split("\n")

            for x in csv_data:
                fields=x.split(",")
                created=Student.objects.update_or_create(
                    studentname=fields[0],
                    coursename=fields[1],
                    courseid=fields[2],
                    semester=fields[3],
                    semester_mark=fields[4],
                    semester_attendance=fields[5],
                    status=fields[6],
                )
            url=reverse('admin:index')
            return HttpResponseRedirect(url)

        form=CsvImportForm()
        data={"form":form}
        return render(request,"admin/csv_upload.html",data)