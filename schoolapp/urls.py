from django.urls import path

from schoolapp import views

urlpatterns = [
    path('',views.Home,name ='home'),
    path('About', views.About, name='about'),
    path('Services', views.Services, name='services'),
    path('Contact', views.Contact, name='contact'),

    path('SignIn', views.SignIn, name='signin'),
    path('DoSignIn', views.DoSignIn, name='signin'),
    path('DoTeacherSignIn', views.DoTeacherSignIn, name='signin'),

    path('Loginn', views.Loginn, name='login'),
    path('DoLogin', views.Dologin, name='login'),
    path('DoTeacherLogin', views.DoTeacherLogin, name='login'),

    path('TeacherEdit/<str:username>',views.TeacherEdit,name = 'update'),
    path('TeacherUpdate',views.TeacherUpdate, name ='update'),

    path('StudentHome', views.StudentHome, name='home'),
    path('StudentProfileView', views.StudentProfileView, name='view'),
    path('StudentEnter', views.StudentEnter, name='update'),
    path('NotesView', views.NotesView, name='notes'),
    path('TeacherView', views.TeacherView, name='view'),

    path('TeacherHome', views.TeacherHome, name='home'),
    path('StudentView', views.StudentView, name='view'),
    path('NoteHome',views.NoteHome, name = 'home'),
    path('NoteUpload', views.NoteUpload, name='notes'),
    path('DoNoteUpload', views.DoNoteUpload, name='notes'),
    path('EditNote/<str:id>', views.EditNote, name='notes'),
    path('UpdateNote', views.UpdateNote, name='notes'),
    path('DeleteNote/<str:id>', views.DeleteNote, name='delete'),

    path('StudentLogout', views.StudentLogout, name='logout'),
    path('TeacherLogout', views.TeacherLogout, name='logout'),

]