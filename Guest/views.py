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

