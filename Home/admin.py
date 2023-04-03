from django.contrib import admin
from Home.models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    # fields = ["roll_no","email","name"]
    list_display = ["user","First_Name","Last_Name","Course","Class","is_fee_paid","Roll_No","Email","Control_Number","Phone_Number"]
    search_fields = ["user__username","First_Name","Last_Name","Email","Control_Number","Roll_No","Course","Class"]
    list_filter =["Course","Gender","is_fee_paid","Class","Semester"]


class TeacherAdmin(admin.ModelAdmin):
    fields = ["user","Email","Phone_Number"]

    list_display = ["user","First_Name","Last_Name","Phone_Number","Email"]
    search_fields = ["user__username","First_Name","Last_Name","Phone_Number","Email"]
    list_filter = ["Gender"]

class Student_ResultAdmin(admin.ModelAdmin):
    list_display = ["user","control_No","Result","course","Semester","Exam_Fee"]
    search_fields=["user__username","control_No__control_no","course__course"]
    list_filter=["course","Exam_Fee","Result","Semester"]

admin.site.register(Control_No_ForRef)
admin.site.register(Courses_ForRef)
admin.site.register(Result_ForRef)
admin.site.register(Grade_ForRef)
admin.site.register(Exam_ForRef)
admin.site.register(Exam_Fee_ForRef)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student_Result,Student_ResultAdmin)
admin.site.register(ResultisOut_ForRef)