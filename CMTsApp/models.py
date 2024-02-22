from django.db import models

# Create your models here.
class tbl_Admin(models.Model):
    Admin_Name = models.CharField(max_length=50)
    Admin_Email = models.CharField(max_length=50)
    Admin_Password=models.CharField(max_length=50)
    
class tbl_Category(models.Model):
    Category_Name = models.CharField(max_length=50)
    
class tbl_District(models.Model):
    District_Name = models.CharField(max_length=50)
    
class tbl_State(models.Model):
    State_Name = models.CharField(max_length=50)
    
class tbl_Prod_Type(models.Model):
    Prod_type_Name = models.CharField(max_length=50)
    
class tbl_Place(models.Model):
    Place_Name = models.CharField(max_length=50)
    District_Name = models.ForeignKey(tbl_District,on_delete=models.CASCADE)
    
class tbl_SubCategory(models.Model):
    SubCat_Name = models.CharField(max_length=50)
    Category_Id = models.ForeignKey(tbl_Category, on_delete=models.CASCADE)
    
class tbl_Department(models.Model):
    Department_Name = models.CharField(max_length=50)
    
class tbl_Semester(models.Model):
    Semester_Name = models.CharField(max_length=50)
    
class tbl_Subject(models.Model):
    Subject_Name = models.CharField(max_length=50)
    
class tbl_Course(models.Model):
    Course_Name = models.CharField(max_length=50)
    Course_Duration = models.CharField(max_length=50)
    Course_Nusum = models.CharField(max_length=50)
    Department_Name = models.ForeignKey(tbl_Department, on_delete=models.CASCADE)
    
class tbl_Syllabus(models.Model):
    Course_Name = models.ForeignKey(tbl_Course, on_delete=models.CASCADE)
    Semester_Name = models.ForeignKey(tbl_Semester, on_delete=models.CASCADE)
    Department_Name = models.ForeignKey(tbl_Department, on_delete=models.CASCADE)