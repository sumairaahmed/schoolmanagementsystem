from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from schoolapp.models import notes, Student, Teacher


class notesupload(forms.ModelForm):
    class Meta:
        model = notes
        fields = '__all__'
class userform(forms.ModelForm):
    class Meta:
        model=User
        fields = ['first_name','last_name','email']

class studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_pic','address','clas','phone']

class teacherform(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['profile_pic','username','email','subject','phone']