from django.shortcuts import render,redirect
from CMTsApp.models import *
from Guest.models import *
# Create your views here.

def userRegistration(request):
    district = tbl_District.objects.all()
    if request.method=="POST":
        place = tbl_Place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("guest:userRegistration")
    else:
        return render(request,"guest/NewUser.html",{"districtdata":district})

def ajaxplace(request):
    dis = tbl_District.objects.get(id=request.GET.get("did"))
    place = tbl_Place.objects.filter(District_Name=dis)
    return render(request,"guest/AjaxPlace.html",{"placedata":place})

def Test(request):
    District = tbl_District.objects.all()
    Category = tbl_Category.objects.all()
    Test=tbl_Test.objects.all()
    if request.method=="POST":
        place = tbl_Place.objects.get(id=request.POST.get('sel_place'))
        subcat=tbl_SubCategory.objects.get(id=request.POST.get('sel_subcategory'))
        tbl_Test.objects.create(test_name=request.POST.get("testname"),test_period=request.POST.get("testduration"),test_description=request.POST.get("testdescription"),test_amount=request.POST.get("testamount"),subCategory=subcat,place=place)
        return redirect("guest:Test")
    else:
        return render(request,"guest/Test.html",{"categorydata":Category,"districtdata":District,"Testdata":Test})

def Ajaxtest(request):
    cat= tbl_Category.objects.get(id=request.GET.get("did"))
    subcat = tbl_SubCategory.objects.filter(Category_Id=cat)
    return render(request,"guest/Ajaxtest.html",{"subcategorydata":subcat})


def Login(request):
    if request.method=="POST":
        Email=request.POST.get("user_name")
        Password=request.POST.get("password")
        admincount=tbl_Admin.objects.filter(Admin_Email=Email,Admin_Password=Password).count()
        if admincount>0:
            admin=tbl_Admin.objects.get(Admin_Email=Email,Admin_Password=Password) 
            request.session["adminid"]=admin.id
            return redirect("webclass:Home")
        else:
            return render(request,'Guest/Login.html')
    else:
        return render(request,'Guest/Login.html')