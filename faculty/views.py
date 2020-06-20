from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register


# Create your views here.
def index(request):
    return render(request,'faculty/index.html')

def register(request):
     if request.method=="POST":
        student_name = request.POST.get('name', '')
        student_email = request.POST.get('email', '')
        roll_no = request.POST.get('rollno','')
        image = request.POST.get('','')
        course = request.POST.get('course','')
        hostel_floor = request.POST.get('hostelfloor','')
        gender = request.POST.get('gender','')
        hostel = request.POST.get('hostel', '')
        date_in = request.POST.get('datein', '')
        address = request.POST.get('address', '')
        s_contact = request.POST.get('scontact', '')
        p_contact = request.POST.get('pcontact', '')

        register= Register(student_name=student_name, student_email=student_email, roll_no=roll_no, hostel_floor=hostel_floor, image=image, gender=gender, 
        hostel=hostel, course=course, date_in= date_in, address=address, s_contact=s_contact, p_contact=p_contact )
        register.save()
        thank = True
        return render(request, 'faculty/register.html',{'thank':thank})
     else:
        return render(request,'faculty/register.html')

      #  return redirect('registerStudent')