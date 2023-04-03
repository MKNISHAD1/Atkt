from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User



class Courses_ForRef(models.Model):
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.course

    class Meta:
        verbose_name_plural="CourseDataBase"
    
class Result_ForRef(models.Model):
    result=models.CharField(max_length=20)

    def __str__(self):
        return self.result
    
    class Meta:
        verbose_name_plural="ResultDataBase"

class Grade_ForRef(models.Model):
    grade=models.CharField(max_length=2)

    def __str__(self):
        return self.grade
    class Meta:
        verbose_name_plural="GradeDataBase"
    
class Exam_ForRef(models.Model):
    exam=models.CharField(max_length=30)

    def __str__(self):
        return self.exam
    class Meta:
        verbose_name_plural="ATKTExamDataBase"
    
class Exam_Fee_ForRef(models.Model):
    exam_fee=models.FloatField(max_length=15)
    def __str__(self):
        return str(self.exam_fee)
    class Meta:
        verbose_name_plural="ATKTExamFeeDataBase"
    
class Control_No_ForRef(models.Model):
    control_no=models.IntegerField()

    def __str__(self):
        return str(self.control_no)
    class Meta:
        verbose_name_plural="ControlNoDataBase"

class ResultisOut_ForRef(models.Model):
    is_Result_Out=models.BooleanField(default=False,verbose_name="Check is Result is ready to Publish !!!")

    def __str__(self):
        return str(self.is_Result_Out)
    class Meta:
        verbose_name_plural="ResultisOutDataBase"
    


class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=20)
    Middle_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Father_Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=30)
    PRN=models.IntegerField(blank=True)
    Roll_No=models.IntegerField()
    Control_Number=models.IntegerField()
    Profile_Pic=models.ImageField(upload_to = "profiles/%Y/%m/%d",null=True,blank=True)
    Fee_pdf=models.FileField(upload_to="Fee_Pdf/%Y/%m/%d", null=True,blank=True)
    is_fee_paid=models.BooleanField(default=False)
    Phone_Number=models.IntegerField()
    Address=models.CharField(max_length=500,blank=True)
    Course=models.CharField(max_length=30)
    Class=models.CharField(max_length=10)
    Semester=models.IntegerField()
    Gender=models.CharField(max_length=10)
    Added_On=models.DateTimeField(auto_now_add=True,null=True)
    Update_On=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.First_Name+" "+self.Last_Name
    class Meta:
        verbose_name_plural="Student_Information"

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=20)
    Last_Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=50)
    Phone_Number=models.IntegerField()
    Profile_Pic=models.ImageField(upload_to = "profiles/%Y/%m/%d",null=True,blank=True)
    Gender=models.CharField(max_length=10)
    Added_On=models.DateTimeField(auto_now_add=True,null=True)
    Update_On=models.DateTimeField(auto_now=True,null=True)
    
    def __str__(self):
        return self.First_Name+" "+self.Last_Name
    
    class Meta:
        verbose_name_plural="Teacher_Informatioon"

class Student_Result(models.Model):
    control_No=models.OneToOneField(Control_No_ForRef,on_delete=models.CASCADE)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Courses_ForRef,on_delete=models.CASCADE)
    Semester=models.IntegerField(null=True,blank=True)
    Result=models.ForeignKey(Result_ForRef,on_delete=models.CASCADE)
    Grade=models.ForeignKey(Grade_ForRef,on_delete=models.CASCADE)
    SGPI=models.FloatField(max_length=5)
    Exam=models.ForeignKey(Exam_ForRef,on_delete=models.CASCADE)
    Subject=models.CharField(max_length=200)
    Exam_Fee=models.ForeignKey(Exam_Fee_ForRef,on_delete=models.CASCADE)
    publish_Result=models.BooleanField(default=False,verbose_name="Check if Result is ready")

    def __str__(self):
        return str(self.Result)
    
    class Meta:
        verbose_name_plural="Student_Result_Information"



