from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from schoolapp.forms import notesupload, userform, studentform, teacherform
from schoolapp.models import Teacher, notes, Student


def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

def signin(request):
    return render(request,'register.html')
def signinf(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username already exists")
                return signin(request)
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email already exists")
                return signin(request)
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return loginn(request)

        else:
            messages.info(request,"Password doesnot match")
            return redirect('signin')
def teachersigninf(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if Teacher.objects.filter(username = username).exists():
                messages.info(request,"Username already exists")
                return signin(request)
            elif Teacher.objects.filter(email = email).exists():
                messages.info(request,"Email already exists")
                return signin(request)
            else:
                user = Teacher(username = username,email = email,password = password1)
                user.save()
                return teacheredit(request,username)
        else:
            messages.info(request,"Password doesnot match")
            return signin(request)

def teacherloginf(request):
    teacher = Teacher.objects.get(username=request.POST['username'])
    if teacher.password == request.POST['password']:
        request.session['name'] = teacher.username

        return render(request, 'teacherhome.html', {'teacher':teacher})
    else:
        messages.info(request, 'invalid username or password')
        return loginn(request)
def teacheredit(request,username):
    teacher = Teacher.objects.get(username= username)
    if teacher!= None:
        return render(request,'teacherinfo.html',{'teacher':teacher})


def teacherupdate(request):
    if request.method == 'POST':
        teacher = Teacher.objects.get(username=request.POST.get("username",''))
        if teacher!= None:
            if request.FILES.get('profile')!=None:
                file = request.FILES['profile']
                fs = FileSystemStorage()
                profile_pic = fs.save(file.name,file)
            else:
                profile_pic = None
            if profile_pic!= None:
                teacher.profile_pic = profile_pic
            teacher.name = request.POST.get('name','')
            teacher.email = request.POST.get('email','')
            teacher.subject = request.POST.get('subject','')
            teacher.phone = request.POST.get('phone','')
            teacher.save()

            messages.info(request,'updated successfully')
            return teacherhome(request)

        else:
            messages.info(request,'Error Loading')
            return home(request)
    else:
        messages.info(request,'method not allowed')



def teacherlogout(request):
    try:
        del request.session['name']
    except KeyError:
        pass
    return loginn(request)

def loginn(request):
    return render(request,'studentteacherlogin.html')

def loginf(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['name'] = username
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return studenthome(request)
        else:
            return loginn(request)
def studentlogout(request):
    logout(request)
    return loginn(request)

def teacherhome(request):
    return render(request,'teacherhome.html')
def noteupload(request):
    return render(request, 'notesupload.html')

def notesuploading(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        module = request.POST.get('module')
        note = request.FILES.get('notes')
        notez = notes(subject=subject,module=module,notess=note)
        notez.save()
        messages.info(request,'uploaded')
        return noteshome(request)
    else:
        messages.info(request,'error uploading')
        return noteupload(request)



def studenthome(request):
    return render(request,'studenthome.html')
def notesview(request):
    note = notes.objects.all()
    return render(request,'notesview.html',{'notes':note})

def studentview(request):
    return render(request,'studentview.html')
def studententer(request):
    user = userform()
    student = studentform()
    if request.method == 'POST':
        user = userform(request.POST, instance=request.user)
        student = studentform(request.POST, request.FILES, instance=request.user.student)
        if user.is_valid() and student.is_valid():
            user.save()
            student.save()
            messages.info(request,'Updated Successfully')
            return studentview(request)
    return render(request,'studententer.html',{'user':user,'student':student})

def viewstudent(request):
    user = User.objects.all()
    student = Student.objects.all()
    return render(request,'studentteacherview.html',{'user':user,'student':student})

def viewteacher(request):
    teacher = Teacher.objects.all()
    return render(request,'teacherview.html',{'teacher':teacher})

def noteshome(request):
    note = notes.objects.all()
    return render(request,'noteshome.html',{'note':note})
def editnotes(request, id):
    note = notes.objects.get(id = id)
    print(note)
    if note != None:
        return render(request, 'noteupdate.html', {'note': note})

def noteupdate(request):
    if request.method == 'POST':
        note = notes.objects.get(id=request.POST.get('id',''))
        if note is not None:
            if request.FILES.get('notes')is not None:
                file = request.FILES['notes']
                fs = FileSystemStorage()
                notess = fs.save(file.name,file)
            else:
                notess = None
            if notess is not None:
                note.notess = notess
            note.subject = request.POST.get('subject','')
            note.module = request.POST.get('module','')
            note.save()

            messages.info(request,'updated')
            return redirect("editnotes/"+str(note.id)+"")

        else:
            messages.info(request,'Error Loading')
            return home(request)
    else:
        messages.info(request,'method not allowed')

def deletenotes(request, id):
    note = notes.objects.get(id = id)
    note.delete()
    messages.info(request,'Deleted')
    return noteshome(request)
# Create your views here.


