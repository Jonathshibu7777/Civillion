from django.shortcuts import render,redirect
from CMTsApp.models import *

# Create your views here.
def admin(request):
    adminData=tbl_Admin.objects.all()
    if request.method == 'POST':
        Admin_Name = request.POST.get('AdminName')
        Admin_Email = request.POST.get('AdminEmail')
        Admin_Password = request.POST.get('AdminPassword')
        tbl_Admin.objects.create(Admin_Name=Admin_Name,Admin_Email=Admin_Email, Admin_Password=Admin_Password)
        return render(request,"CMTsApp/Admin.html",{"admindata":adminData})
    else:
        return render(request,"CMTsApp/Admin.html",{"admindata":adminData})
    
def delete_admin(request,id):
    tbl_Admin.objects.get(id=id).delete()
    return redirect("webclass:Admin")

def edit_admin(request,id):
    editadmin=tbl_Admin.objects.get(id=id)
    if request.method == "POST":
        editadmin.Admin_Name =(request.POST.get('AdminName'))
        editadmin.Admin_Email =(request.POST.get('AdminEmail'))
        editadmin.Admin_Password =(request.POST.get('AdminPassword'))
        editadmin.save()
        return redirect("webclass:Admin")
    else:
        return render(request,"CMTsApp/Admin.html",{"editadmin":editadmin})
    
def Category(request):
    CatData=tbl_Category.objects.all()
    if request.method == 'POST':
        Category_Name = request.POST.get('CategoryName')
        tbl_Category.objects.create(Category_Name=Category_Name)
        return render(request,"CMTsApp/Category.html",{"catdata":CatData})
    else:
        return render(request,"CMTsApp/Category.html",{"catdata":CatData})
    
def delete_cat(request,id):
    tbl_Category.objects.get(id=id).delete()
    return redirect("webclass:Category")

def edit_cat(request,id):
    editcat=tbl_Category.objects.get(id=id)
    if request.method == "POST":
        editcat.Category_Name =(request.POST.get('CategoryName'))
        editcat.save()
        return redirect("webclass:Category")
    else:
        return render(request,"CMTsApp/Category.html",{"editcat":editcat})

def SubCat(request):
    CatData=tbl_Category.objects.all()
    SubCatData=tbl_SubCategory.objects.all()
    if request.method == "POST":
        SubCat_Name = request.POST.get("SubCategoryName")
        Category= tbl_Category.objects.get(id=request.POST.get('sel_Category'))
        tbl_SubCategory.objects.create(SubCat_Name=SubCat_Name,Category_Id = Category)
        return redirect(request,"CMTsApp/SubCat.html",{"subcatdata":SubCatData})
    else:
        return render(request,"CMTsApp/SubCat.html",{"categorydata":CatData,"subcatdata":SubCatData})

def delete_SubCat(request,id):
    tbl_SubCategory.objects.get(id=id).delete()
    return redirect("webclass:SubCat")

def District(request):
    DistrictData=tbl_District.objects.all()
    if request.method == 'POST':
        District_Name = request.POST.get('DistrictName')
        tbl_District.objects.create(District_Name=District_Name)
        return render(request,"CMTsApp/District.html",{"districtdata":DistrictData})
    else:
        return render(request,"CMTsApp/District.html",{"districtdata":DistrictData})
    
def delete_district(request,id):
    tbl_District.objects.get(id=id).delete()
    return redirect("webclass:District")

def edit_district(request,id):
    edit_district=tbl_District.objects.get(id=id)
    if request.method == "POST":
        edit_district.District_Name =(request.POST.get('DistrictName'))
        edit_district.save()
        return redirect("webclass:District")
    else:
        return render(request,"CMTsApp/District.html",{"editdistrict":edit_district})

def Place(request):
    DistrictData =tbl_District.objects.all()
    PlaceData = tbl_Place.objects.all()
    if request.method == "POST":
        Place_Name = request.POST.get('PlaceName')
        dis= tbl_District.objects.get(id=request.POST.get('sel_district'))
        tbl_Place.objects.create(Place_Name=Place_Name,District_Name = dis)
        return render(request,"CMTsApp/Place.html",{"placedata":PlaceData})
    else:
        return render(request,"CMTsApp/Place.html",{"placedata":PlaceData,"districtdata":DistrictData})
    
def delete_place(request,id):
    tbl_Place.objects.get(id=id).delete()
    return redirect("webclass:Place")

def edit_place(request,id):
    District=tbl_District.objects.all()
    editdata=tbl_Place.objects.get(id=id)
    if request.method == "POST":
        editdata.Place_Name=request.POST.get('PlaceName')
        dis=tbl_District.objects.get(id=request.POST.get('sel_district'))
        editdata.District_Name = dis
        editdata.save()
        return redirect("webclass:Place")
    else:
        return render(request,"CMTsApp/Place.html",{"editdata":editdata,"districtdata":District}) 
    
def Department(request):
    DepartmentData=tbl_Department.objects.all()
    if request.method == 'POST':
        Department_Name = request.POST.get('DepartmentName')
        tbl_Department.objects.create(Department_Name=Department_Name)
        return render(request,"CMTsApp/Department.html",{"departmentdata":DepartmentData})
    else:
        return render(request,"CMTsApp/Department.html",{"departmentdata":DepartmentData})
    
def delete_department(request,id):
    tbl_Department.objects.get(id=id).delete()
    return redirect("webclass:Department")

def edit_department(request,id):
    edit_department=tbl_Department.objects.get(id=id)
    if request.method == "POST":
        edit_department.Department_Name =(request.POST.get('DepartmentName'))
        edit_department.save()
        return redirect("webclass:Department")
    else:
        return render(request,"CMTsApp/Department.html",{"editdepartment":edit_department})
    
def Semester(request):
    SemesterData =tbl_Semester.objects.all()
    if request.method == 'POST':
        Semester_Name = request.POST.get('SemesterName')
        tbl_Semester.objects.create(Semester_Name=Semester_Name)
        return render(request,"CMTsApp/Semester.html",{"semesterdata":SemesterData})
    else:
        return render(request,"CMTsApp/Semester.html",{"semesterdata":SemesterData})
    
def delete_semester(request,id):
    tbl_Semester.objects.get(id=id).delete()
    return redirect("webclass:Semester")

def edit_semester(request,id):
    edit_semester=tbl_Semester.objects.get(id=id)
    if request.method == "POST":
        edit_semester.Semester_Name =(request.POST.get('SemesterName'))
        edit_semester.save()
        return redirect("webclass:Semester")
    else:
        return render(request,"CMTsApp/Semester.html",{"editsemester":edit_semester})
    
def Subject(request):
    SubjectData =tbl_Subject.objects.all()
    if request.method == 'POST':
        Subject_Name = request.POST.get('SubjectName')
        tbl_Subject.objects.create(Subject_Name=Subject_Name)
        return render(request,"CMTsApp/Subject.html",{"subjectdata":SubjectData})
    else:
        return render(request,"CMTsApp/Subject.html",{"subjectdata":SubjectData})
    
def delete_subject(request,id):
    tbl_Subject.objects.get(id=id).delete()
    return redirect("webclass:Subject")

def edit_subject(request,id):
    edit_subject=tbl_Subject.objects.get(id=id)
    if request.method == "POST":
        edit_subject.Seubject_Name =(request.POST.get('SubjectName'))
        edit_subject.save()
        return redirect("webclass:Subject")
    else:
        return render(request,"CMTsApp/Subject.html",{"editsubject":edit_subject})
    
def Course(request):
    CourseData =tbl_Course.objects.all()
    DepartmentData = tbl_Department.objects.all()
    if request.method == "POST":
        Course_Name = request.POST.get('CourseName')
        Course_Duration = request.POST.get('CourseDuration')
        Course_Nusum = request.POST.get('CourseNumber')
        dept= tbl_Department.objects.get(id=request.POST.get('sel_department'))
        tbl_Course.objects.create(Course_Name=Course_Name,Course_Duration=Course_Duration,Course_Nusum=Course_Nusum,Department_Name = dept)
        return redirect("webclass:Course")
    else:
        return render(request,"CMTsApp/Course.html",{"coursedata":CourseData,"departmentdata":DepartmentData})
    
def delete_course(request,id):
    tbl_Course.objects.get(id=id).delete()
    return redirect("webclass:Course")

def syllabus(request):
    CourseData =tbl_Course.objects.all()
    DepartmentData = tbl_Department.objects.all()
    SemesterData = tbl_Semester.objects.all()
    SyllabusData = tbl_Syllabus.objects.all()
    if request.method == "POST":
        course=tbl_Course.objects.get(id=request.POST.get('sel_course'))
        dept= tbl_Department.objects.get(id=request.POST.get('sel_department'))
        Sem=tbl_Semester.objects.get(id=request.POST.get('sel_semester'))
        tbl_Syllabus.objects.create(Course_Name=course,Semester_Name=Sem,Department_Name=dept)
        return redirect("webclass:syllabus")
    else:
        return render(request,"CMTsApp/syllabus.html",{"coursedata":CourseData,"departmentdata":DepartmentData,"semesterdata":SemesterData,"syllabus":SyllabusData})
    
def delete_syllabus(request,id):
    tbl_Syllabus.objects.get(id=id).delete()
    return redirect("webclass:syllabus")