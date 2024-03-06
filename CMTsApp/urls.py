from django.urls import path
from CMTsApp import views

app_name='webclass'
urlpatterns = [
    path('Home/',views.home,name="Home"),

    path('Admin/', views.admin,name="Admin"),
    path('delete_admin/<int:id>',views.delete_admin,name="delete_admin"),
    path('edit_admin/<int:id>',views.edit_admin,name="edit_admin"),
    
    path('Category/', views.Category,name="Category"),
    path('delete_cat/<int:id>',views.delete_cat,name="delete_cat"),
    path('edit_cat/<int:id>',views.edit_cat,name="edit_cat"),
    
    path('District/', views.District,name="District"),
    path('delete_district/<int:id>',views.delete_district,name="delete_district"),
    path('edit_district/<int:id>',views.edit_district,name="edit_district"),
    
    path('Place/', views.Place,name="Place"),
    path('delete_place/<int:id>',views.delete_place,name="delete_place"),
    path('edit_place/<int:id>',views.edit_place,name="edit_place"),
    
    path('SubCat/', views.SubCat,name="SubCat"),
    path('delete_SubCat/<int:id>',views.delete_SubCat,name="delete_SubCat"),
    
]