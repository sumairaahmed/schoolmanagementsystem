from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from schoolapp.forms import notesupload, userform, studentform, teacherform
from schoolapp.models import Teacher, notes, Student


def Home(request):
    return render(request,'home.html')
def About(request):
    return render(request,'about.html')
def Services(request):
    return render(request,'services.html')
def Contact(request):
    return render(request,'contact.html')

def SignIn(request):
    return render(request,'register.html')
def DoSignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username already exists")
                return SignIn(request)
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email already exists")
                return SignIn(request)
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return Loginn(request)

        else:
            messages.info(request,"Password doesnot match")
            return SignIn(request)

def DoTeacherSignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if Teacher.objects.filter(username = username).exists():
                messages.info(request,"Username already exists")
                return SignIn(request)
            elif Teacher.objects.filter(email = email).exists():
                messages.info(request,"Email already exists")
                return SignIn(request)
            else:
                user = Teacher(username = username,email = email,password = password1)
                user.save()
                return TeacherEdit(request,username)
        else:
            messages.info(request,"Password doesnot match")
            return SignIn(request)

def TeacherEdit(request,username):
    teacher = Teacher.objects.get(username= username)
    if teacher!= None:
        return render(request,'teacherinfo.html',{'teacher':teacher})

def TeacherUpdate(request):
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

            messages.success(request,'Updated Successfully')
            return TeacherHome(request)

        else:
            messages.info(request,'Error Loading,Contact Admin')
            return Home(request)
    else:
        messages.info(request,'method not allowed')


def Loginn(request):
    return render(request,'studentteacherlogin.html')

def Dologin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['name'] = username
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return StudentHome(request)
        else:
            return Loginn(request)



def DoTeacherLogin(request):
    teacher = Teacher.objects.get(username=request.POST['username'])
    if teacher.password == request.POST['password']:
        request.session['name'] = teacher.username

        return render(request, 'teacherhome.html', {'teacher':teacher})
    else:
        messages.info(request, 'invalid username or password')
        return Loginn(request)

def TeacherLogout(request):
    try:
        del request.session['name']
    except KeyError:
        pass
    return Loginn(request)


def StudentHome(request):
    return render(request,'studenthome.html')

def StudentProfileView(request):
    return render(request,'studentview.html')

def StudentEnter(request):
    user = userform()
    student = studentform()
    if request.method == 'POST':
        user = userform(request.POST, instance=request.user)
        student = studentform(request.POST, request.FILES, instance=request.user.student)
        if user.is_valid() and student.is_valid():
            user.save()
            student.save()
            messages.success(request,'Updated Successfully')
            return StudentView(request)
    return render(request,'studententer.html',{'user':user,'student':student})

def NotesView(request):
    note = notes.objects.all()
    return render(request,'notesview.html',{'notes':note})

def TeacherView(request):
    teacher = Teacher.objects.all()
    return render(request,'teacherview.html',{'teacher':teacher})

def StudentLogout(request):
    logout(request)
    return Loginn(request)

def TeacherHome(request):
    return render(request,'teacherhome.html')

def NoteHome(request):
    note = notes.objects.all()
    return render(request,'noteshome.html',{'note':note})

def NoteUpload(request):
    return render(request, 'notesupload.html')

def DoNoteUpload(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        module = request.POST.get('module')
        note = request.FILES.get('notes')
        notez = notes(subject=subject,module=module,notess=note)
        notez.save()
        messages.success(request,'Uploaded')
        return NoteHome(request)
    else:
        messages.error(request,'Error Uploading')
        return NoteUpload(request)

def StudentView(request):
    user = User.objects.all()
    student = Student.objects.all()
    return render(request,'studentteacherview.html',{'user':user,'student':student})

def EditNote(request, id):
    note = notes.objects.get(id = id)
    print(note)
    if note != None:
        return render(request, 'noteupdate.html', {'note': note})

def UpdateNote(request):
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

            messages.success(request,'Updated')
            return redirect("editnotes/"+str(note.id)+"")

        else:
            messages.info(request,'Error Loading')
            return TeacherHome(request)
    else:
        messages.info(request,'Method not allowed')

def DeleteNote(request, id):
    note = notes.objects.get(id = id)
    note.delete()
    messages.info(request,'Deleted')
    return NoteHome(request)
# Create your views here.


