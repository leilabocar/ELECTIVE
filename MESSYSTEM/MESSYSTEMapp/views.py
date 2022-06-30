from ast import dump
from multiprocessing import context
from unicodedata import name
from urllib import response
from django.contrib.auth import get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .filters import *
from django.contrib import messages
from .decorators import *
from django.core.mail import send_mail

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import SimpleDocTemplate


def homepage(request):
    logout(request)
    announcement = make_announcement.objects.last()
    return render(request, 'files/homepage.html',{'announcement': announcement})

def signin(request):
    form = loginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)
            user = authenticate(request, username=username, password=password)      
            if user is not None and user.userType == 'Admin':
                login(request, user)
                return redirect('Admin_Homepage')
            if user is not None and user.userType == 'Student':
                login(request, user)
                return redirect('Student_History_Transaction', username=user.username)
            if user is not None and user.userType == 'Adviser':
                login(request, user)
                return redirect('Distribution_and_Retrieval', user.pk==user.pk)
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('Login')
    return render(request, 'files/login2.html', {'form': form, 'msg':msg})

#------------------------------------------Admin
@login_required
def adminhomepage(request):
    if request.user.is_authenticated and request.user.userType == "Admin":
        form = announceForm()
        rec_count = studentInfo.objects.filter(modules='Receive').count()
        ret_count = studentInfo.objects.filter(modules='Return').count()
        total_count = studentInfo.objects.all().count()
        if request.method =='POST':
            form = announceForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Admin_Homepage')
            else:
                print('error')
    else:
        return redirect('Logout')
        
    return render(request, 'files/adminhomepage.html', {'form': form,
    'rec_count':rec_count,
    'ret_count':ret_count,
    'total_count':total_count})

@login_required
def adminFAD(request):
    if request.user.is_authenticated and request.user.userType == "Admin":
        scholarship_list = scholarship.objects.all()
        studentInfo_list = studentInfo.objects.all()
        form = scholarshipForm()
        if request.method =='POST':
            form = scholarshipForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Admin_Distribution')
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('Admin_Distribution')
    else:
        return redirect('Logout')
    return render(request, 'files/Admin(F.A Distribution).html', {'scholarship_list':scholarship_list,
    'form': form,
    'studentInfo_list':studentInfo_list})

@login_required
def register(request):
    if request.user.is_authenticated and request.user.userType == "Admin":
        form = StudentSignupForm()
        if request.method == 'POST':
            form = StudentSignupForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data.get('email')
                infomessages = "Lrn: " + form.cleaned_data.get('lrn') + " // " + "Username: " +form.cleaned_data.get('username') + " // " "Password: " +form.cleaned_data.get('password2') + " // " + "Grade Level: " +form.cleaned_data.get('gradelvl') + " // " + "Section: " + form.cleaned_data.get('section')
                send_mail(
                'Successfully Created - MES',
                infomessages,
                'andrewleilaraqueljustin@gmail.com',
                [email],
                fail_silently=False,
            )
                form.save()
                return redirect('Admin_Homepage')
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('Register')
    else:
        return redirect('Logout')
    return render(request, 'files/register.html', {'form': form})

@login_required
def AdminFAD_Delete(request, lrn_scholarship):
    if request.user.is_authenticated and request.user.userType == "Admin":
        scholarship.objects.filter(lrn_scholarship=lrn_scholarship).delete()
        return redirect('Admin_Distribution')
    else:
        return redirect('Logout')

@login_required
def AdminFAD_Update(request, lrn_scholarship):
    if request.user.is_authenticated and request.user.userType == "Admin":
        scholar = scholarship.objects.get(lrn_scholarship=lrn_scholarship)
        form = scholarshipForm(request.POST or None, instance=scholar)
        if form.is_valid():
            form.save()
            return redirect('Admin_Distribution')
    else:
        return redirect('Logout')
    return render(request, 'files/Admin(F.A Distribution).html', {'scholar':scholar,'form':form})

@login_required
def adminFA(request):
    if request.user.is_authenticated and request.user.userType == "Admin":
        scholar_list = studentInfo.objects.filter(status='Approved')
    else:
        return redirect('Logout')
    return render(request, 'files/Admin(Financial Assistance).html',{'scholar_list':scholar_list})

@login_required
def student_transaction(request):
    if request.user.is_authenticated and request.user.userType == "Admin":
        student = studentInfo.objects.all()
        myFilter = studentFilter(request.GET, queryset=student)
        student = myFilter.qs
    else:
        return redirect('Logout')
    return render(request, 'files/student-transaction.html', {'student':student,
    'myFilter':myFilter})

def pdf_assistance(request):
    #create byteststream buffer
    buf = io.BytesIO()
    #create document template
    pdf = SimpleDocTemplate(buf, pagesize=letter)
    #content
    scholar_list = studentInfo.objects.filter(status='Approved')
    data = [['Lrn','Username','Quarter','Week','Modules','Status',]]
    for scholar in scholar_list:
        data.append([scholar.lrn_student_id,scholar.username,scholar.quarter,scholar.week,scholar.modules,scholar.status])
    elems = []
    #table
    elems.append(Table(data))
    pdf.build(elems)
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Admin_Approved_Student.pdf')

def pdf_student_transaction(request):
    #create byteststream buffer
    buf = io.BytesIO()
    #create document template
    pdf = SimpleDocTemplate(buf, pagesize=letter)
    #content
    students = studentInfo.objects.all()
    data = [['Lrn','Username','Quarter','Week','Modules','Status']]
    for student in students:
        data.append([student.lrn_student_id,student.username,student.quarter,student.week,student.modules,student.status])
    elems = []
    #table
    elems.append(Table(data))
    pdf.build(elems)
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename='Admin_Student_Transaction.pdf')

def pdf_distribution(request):
    #create byteststream buffer
    buf = io.BytesIO()
    #create document template
    pdf = SimpleDocTemplate(buf, pagesize=letter)
    #content
    scholarship_list = scholarship.objects.all()
    data = [['Lrn','Username','Amount']]
    for scholar in scholarship_list:
        data.append([scholar.lrn_scholarship_id,scholar.username,scholar.amount])
    elems = []
    #table
    elems.append(Table(data))
    pdf.build(elems)
    buf.seek(0)
    #filename
    return FileResponse(buf, as_attachment=True, filename='Admin_Scholars.pdf')

#------------------------------------------TEACHER
@login_required
def distribution_and_retrieval(request, lrn_student):
    if request.user.is_authenticated and request.user.userType == "Adviser":
        student = studentInfo.objects.filter(lrn_student=lrn_student).first()
        if request.method == 'POST':
            form = distributionRetrievalForm(request.POST or None, instance=student)
            if form.is_valid():
                form.save()
                return redirect('Distribution_and_Retrieval',lrn_student==lrn_student)
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('Distribution_and_Retrieval',lrn_student==lrn_student)
        else:
            form = distributionRetrievalForm(request.POST or None, instance=student)
    else:
        return redirect('Logout')
    return render(request, 'files/distribution-and-retrieval.html',{'student':student,'form':form})

@login_required
def teacher_transaction(request):
    if request.user.is_authenticated and request.user.userType == "Adviser":
        studentInfo_list = studentInfo.objects.all()
    else:
        return redirect('Logout')
    return render(request, 'files/teacher-transaction.html',
        {'studentInfo_list': studentInfo_list})

@login_required
def teacher_transaction_delete(request, lrn_student):
    if request.user.is_authenticated and request.user.userType == "Adviser":
        studentInfo.objects.filter(lrn_student=lrn_student).delete()
        return redirect('Teacher_Transaction')
    else:
        return redirect('Logout')

@login_required
def teacher_transaction_update(request, lrn_student):
    if request.user.is_authenticated and request.user.userType == "Adviser":
        student = studentInfo.objects.get(lrn_student=lrn_student)
        form = distributionRetrievalForm(request.POST or None, instance=student)
        if form.is_valid():
            form.save()
            return redirect('Teacher_Transaction')
    else:
        return redirect('Logout')
    return render(request, 'files/distribution-and-retrieval.html', {'student':student,'form':form})

def pdf_teacher_transaction(request):
    #create byteststream buffer
    buf = io.BytesIO()
    #create document template
    pdf = SimpleDocTemplate(buf, pagesize=letter)
    #content
    students = studentInfo.objects.all()
    data = [['Lrn','Username','Quarter','Week','Modules','Status',]]
    #loop
    for student in students:
        data.append([student.lrn_student_id,student.username,student.quarter,student.week,student.modules,student.status])
    elems = []
    #table
    elems.append(Table(data))
    pdf.build(elems)
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='Teacher_Transaction.pdf')

#--------------------------------------------------student
@login_required
def student_history_transaction(request, username):
    if request.user.is_authenticated and request.user.userType == "Student":
        information1 = registration.objects.filter(username=username)
        information2 = studentInfo.objects.filter(username=username)

        zipped = zip(information1, information2)
    else:
        return redirect('Logout')
    return render(request, 'files/student-history-transaction.html',{'zipped':zipped})

def logout_view(request):
    logout(request)
    return redirect('Login')
