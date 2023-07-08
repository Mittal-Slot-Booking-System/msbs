from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import student,faculty,applicant
from .forms import StudentForm, FacultyForm
from django.urls import reverse

def index(request):
    form = None
    form_type=None
    if request.method == 'POST':
       
            
        form_type = request.POST.get('form_type')
        
        if form_type == 'student_form':
            
            form = StudentForm(request.POST)
            try:
                
                if form.is_valid():
                    
                    form_type=request.POST.get('form_type')
                    firstname=request.POST.get('firstname')
                    lastname=request.POST.get('lastname')
                    guardianfirstname=request.POST.get('guardianfirstname')
                    guardianlastname=request.POST.get('guardianlastname')
                    age=request.POST.get('age')
                    gender=request.POST.get('gender')
                    mobilenumber=request.POST.get('mobilenumber')
                    entrynumber=request.POST.get('entrynumber')
                    department=request.POST.get('department')
                    hostel=request.POST.get('hostel')
                    roomnumber=request.POST.get('roomnumber')
                    emergencynumber=request.POST.get('emergencynumber')
                    address=request.POST.get('address')
                    swim=request.POST.get('swim')
                    form.cleaned_data.update({
                        'form_type':form_type,
                        'firstname': firstname,
                        'lastname': lastname,
                        'guardianfirstname': guardianfirstname,
                        'guardianlastname': guardianlastname,
                        'age':age,
                        'gender': gender,
                        'mobilenumber': mobilenumber,
                        'entrynumber': entrynumber,
                        'department': department,
                        'hostel': hostel,
                        'roomnumber': roomnumber,
                        'emergencynumber': emergencynumber,
                        'address': address,
                        'swim': swim,
                        })
                    form.save()
                    return HttpResponse("SAVED")
                    
                # if form.errors:
                #     print(form.errors)
                    
            except:
                print("hi")
            # if form.errors:
            #     print("*******")
            #     print(form.errors)
            
        elif form_type == 'faculty_form':
            form = FacultyForm(request.POST)
            try:
                if form.is_valid():
                    Name = request.POST.get('Name')
                    Designation = request.POST.get('Designation')
                    Family = request.POST.get('Family')
                    Relation = request.POST.get('Relation')
                    age = request.POST.get('age')
                    gender = request.POST.get('gender')
                    mobilenumber = request.POST.get('mobilenumber')
                    EmpCode = request.POST.get('EmpCode')
                    department = request.POST.get('department')
                    emergencynumber = request.POST.get('emergencynumber')
                    address = request.POST.get('address')
                    swim = request.POST.get('swim')
                    form.cleaned_data.update({
                        'Name': Name,
                        'Designation': Designation,
                        'Family': Family,
                        'Relation': Relation,
                        'age':age,
                        'gender': gender,
                        'mobilenumber': mobilenumber,
                        'EmpCode': EmpCode,
                        'department': department,
                        'emergencynumber': emergencynumber,
                        'address': address,
                        'swim': swim,
                        })
                form.save()
                if form.errors:
                    print(form.errors)
                return HttpResponse("SAVED")

            except:
                if form.errors:
                    print(form.errors)
                print("hi")
            # if form.errors:
            #     print(form.errors)
    
    template=loader.get_template('form.html')
    return render(request,"form.html",{'form':form,'form_type':form_type})

    # if request.method == "POST":
        
    #     app=request.POST['applicant']
        
        
    #     entry=applicant(app=app,)
    #     entry.save()
    #     return render(request,"form.html",{'applicant':app})
       
    
    # else:
    #     template=loader.get_template('form.html')
    #     return HttpResponse(template.render({},request))
def all(request):
    all=student.objects.all().values()
    template=loader.get_template('all.html')
    context={
        'all':all,
    }
    return HttpResponse(template.render(context,request))
def main(request):
    template=loader.get_template('form.html')
    return HttpResponse(template.render({},request))
