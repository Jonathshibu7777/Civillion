from django.urls import path
from Guest import views
app_name="guest"
urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    
]