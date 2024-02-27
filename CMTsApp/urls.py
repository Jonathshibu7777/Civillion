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
    
    path('Department/', views.Department,name="Department"),
    path('delete_department/<int:id>',views.delete_department,name="delete_department"),
    path('edit_department/<int:id>',views.edit_department,name="edit_department"),
    
    path('Semester/', views.Semester,name="Semester"),
    path('delete_semester/<int:id>',views.delete_semester,name="delete_semester"),
    path('edit_semester/<int:id>',views.edit_semester,name="edit_semester"),
    
    path('Subject/', views.Subject,name="Subject"),
    path('delete_subject/<int:id>',views.delete_subject,name="delete_subject"),
    path('edit_subject/<int:id>',views.edit_subject,name="edit_subject"),
    
    path('Course/', views.Course,name="Course"),
    path('delete_course/<int:id>',views.delete_course,name="delete_course"),
    
    path('syllabus/', views.syllabus,name="syllabus"),
    path('delete_syllabus/<int:id>',views.delete_syllabus,name="delete_syllabus"),
    
]