from django.urls import path

from schoolapp import views

urlpatterns = [
    path('',views.home,name ='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('loginn', views.loginn, name='login'),
    path('signin', views.signin, name='signin'),
    path('studenthome', views.studenthome, name='home'),
    path('teacherhome', views.teacherhome, name='home'),
    path('studentview', views.studentview, name='view'),
    path('studententer', views.studententer, name='update'),
    path('loginf', views.loginf, name='login'),
    path('teacherloginf', views.teacherloginf, name='login'),
    path('signinf', views.signinf, name='signin'),
    path('teachersigninf', views.teachersigninf, name='signin'),
    path('viewstudent', views.viewstudent, name='view'),
    path('viewteacher', views.viewteacher, name='view'),
    path('teacheredit/<str:username>',views.teacheredit,name = 'update'),
    path('teacherupdate',views.teacherupdate, name ='update'),
    path('noteshome',views.noteshome, name = 'home'),
    path('deletenotes/<str:id>', views.deletenotes, name='delete'),

    path('studentlogout', views.studentlogout, name='login'),
    path('teacherlogout', views.teacherlogout, name='login'),
    path('noteupload',views.noteupload,name ='notes'),
    path('editnotes/<str:id>', views.editnotes, name='notes'),
    path('noteupdate', views.noteupdate, name='notes'),

    path('notesuploading', views.notesuploading, name='notes'),
    path('notesview', views.notesview, name='notes'),

]