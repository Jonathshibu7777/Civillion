from django.urls import path
from Guest import views
app_name="guest"
urlpatterns = [

    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Test/',views.Test,name="Test"),
    path('Ajaxtest/',views.Ajaxtest,name="Ajaxtest"),
    path('Login/',views.Login,name="Login"),
]