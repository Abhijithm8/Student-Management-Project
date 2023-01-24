from django.urls import path

from studentapp import views

urlpatterns =[
    path('reg',views.reg_fun,name='reg'),                                #it will redirect to register.html page
    path('regdata',views.regdata_fun),                                   #it will create super account
    path('',views.log_fun,name='log'),                                   #it will display login.html page
    path('logdata',views.logdata_fun),                                   #it will redirect to register.html page it will creste super user
    path('home',views.home_fun,name='home'),
    path('add_students',views.addstudent_fun,name='add'),                #it will redirect to addstudent.html
    path('readdata',views.readdata_fun),                                 #it will insert records into studenttable
    path('display', views.display_fun, name='display'),                   #it will display student data in display.html file
    path('update/<int:id>',views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out')
]