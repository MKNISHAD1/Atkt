"""ATKT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "MkNishad Admin"
admin.site.site_title = "Mk Admin Portal"
admin.site.index_title = "Welcome to MK Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index,name='Home'),
    path('home',views.index,name='Home'),
    path('about',views.about,name='About'),
    path('login',views.loginuser,name='Login'),
    path('data',views.data,name='Data'),
    path('register',views.reguser,name='Register'),
    path('check_user',views.check_user,name="check_user"),
    path('Stud_Dash',views.Stud_dashboard,name="Stud_Dash"),
    path('Tea_Dash',views.Tea_dashboard,name="Tea_Dash"),
    path('logout',views.logoutuser,name='Logout'),
    path('editprofile',views.edit_profile,name='EditProfile'),
    path('changepass',views.change_pass,name='Change_Pass'),
    path('result_form',views.test_check,name='result_form'),
    path('check_user1',views.check_user1,name="check_user1"),
    path('result',views.result,name='result'),
    path('forgot_pass',views.forgotpass,name='forgot_pass'),
    path('reset_password',views.reset_password,name='reset_password'),
    path('Fee_Not_Paid',views.feenotpaid,name='Fee_Not_Paid'),
    path('Result_Not_Out',views.resultnotout,name='Result_Not_Out')
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
