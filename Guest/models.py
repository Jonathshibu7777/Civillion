from django.db import models
from CMTsApp.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_Place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")
    
class tbl_Test(models.Model):
    subCategory = models.ForeignKey(tbl_SubCategory, on_delete=models.CASCADE)
    test_name=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_Place, on_delete=models.CASCADE)
    test_period=models.CharField(max_length=50)
    test_description=models.CharField(max_length=50)
    test_amount=models.CharField(max_length=50)