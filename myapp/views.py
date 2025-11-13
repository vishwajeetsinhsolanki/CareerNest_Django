from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import redirect
import random
from .utils import *
# Create your views here.



# def contactus(request):
#     return render(request,"myapp/contact.html")
def auth(myfun):
    def wrapper(request, *args, **kwargs):
        if 'email' in request.session:
            return myfun(request, *args, **kwargs)
        else:
            print("Authentication Denied!!!")
            return redirect("login")
    return wrapper


def login(request):
    if 'email' in request.session:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Admin':
            aid = Admin.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'aid' : aid
            }
            return render(request,"myapp/index.html",context)
        else:
            return render(request,"myapp/login.html",context)
    else:
        if request.POST:
            # here left email is python variable and right email is coming from html form
            print(">>>>>>>>>>> submit button press <<<<<<<<<<<<<<")
            email = request.POST['email']
            password = request.POST['password']
            print(">>>>>>>>>>>>>>>>EMAIL = ",email)
                            # model_field = python_variable

            try:
                uid = User.objects.get(email = email)
                if uid:
                    if password == uid.password:
                        print("User match!!!") 
                        request.session['email'] = email
                        aid = Admin.objects.get(user_id = uid)
                        context = {
                            'uid' : uid,
                            'aid' : aid
                        }
                        return render(request,"myapp/index.html",context)
                        
                    else:
                        context = {
                            'e_msg' : "Invalid Password!!!"
                        }
                        return render(request,"myapp/login.html",context)
            except:
                print("Invalid Email of Password.")
                context = {
                    'e_msg' : "Invalid Password or Email!!!"
                }
                return render(request,"myapp/login.html",context)
        else:
            print(">>>>>>>>>>> page refresh only <<<<<<<<<<<<<<")
            return render(request,"myapp/login.html")



@auth
def index(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        d_count = Department.objects.all().count()
        f_count = Faculty.objects.all().count()
        c_count = Course.objects.all().count()

        context = {
            'uid' : uid,
            'aid' : aid,
            'd_count' : d_count,
            'f_count' : f_count,
            'c_count' : c_count
        }
        return render(request,"myapp/index.html",context)
    else:
        return render(request,"myapp/login.html")
    
@auth    
def logout(request):
    del request.session['email']
    return redirect("login")

@auth
def add_department(request):
    if request.POST:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Admin':
            aid = Admin.objects.get(user_id = uid)
            department = request.POST['department']
            did = Department.objects.create(user_id = uid,
                                            name = department
                                            )
            context = {
                'uid' : uid,
                'aid' : aid,
                'did' : did,
                's_msg' : "Department added successfully!!!"
            }
            return render(request,"myapp/add_department.html",context)
    else:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Admin':
            aid = Admin.objects.get(user_id = uid)
            context = {
                'uid' : uid,
                'aid' : aid
            }
            return render(request,"myapp/add_department.html",context)

@auth
def view_department(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        dall = Department.objects.all()     # fetch all records from the model
        context = {
            'uid' : uid,
            'aid' : aid,
            'dall' : dall
        }
        return render(request,"myapp/view_department.html",context)
    
@auth
def add_faculty(request):
    if request.POST:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Admin':
            aid = Admin.objects.get(user_id = uid)

            dep = request.POST['department']
            did = Department.objects.get(name=dep)
            print("=======>>>>>> did",did)

            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            contact = request.POST['contact_no']
            pic = request.FILES['pic']
            email = request.POST['email']



            li = ['sd45','ad45','45fd','ety4']
            password = email[3:5] + random.choice(li) + firstname[3:5] + contact[3:6]

            user_id = User.objects.create(email = email,
                                          password = password,
                                          role = "Faculty"
                                          )

            fid = Faculty.objects.create(user_id = user_id,
                                        department_id = did,
                                        firstname = firstname,
                                        lastname = lastname,
                                        contact_no = contact,
                                        pic = pic
                                         )
            
            s_msg = "Successfully Faculty added!!!"

            context = {
                'uid' : uid,
                'aid' : aid,
                's_msg' : s_msg
                
            }
            return render(request,"myapp/add_faculty.html",context)
    else:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Admin':
            aid = Admin.objects.get(user_id = uid)
            d_all = Department.objects.all()
            context = {
                'uid' : uid,
                'aid' : aid,
                'd_all' : d_all
                
            }
            return render(request,"myapp/add_faculty.html",context)
        
@auth
def add_course(request):
    if request.POST:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Admin':
            aid = Admin.objects.get(user_id = uid)
            course = request.POST['course']
            dep = request.POST['department']
            did = Department.objects.get(name = dep)
            cid = Course.objects.create(user_id = uid,
                                        department_id = did,
                                            name = course
                                            )
            context = {
                'uid' : uid,
                'aid' : aid,
                'cid' : cid,
                's_msg' : "course added successfully!!!"
            }
            return render(request,"myapp/add_course.html",context)
    else:
        uid = User.objects.get(email = request.session['email'])
        if uid.role == 'Admin':
            aid = Admin.objects.get(user_id = uid)
            dall = Department.objects.all()
            context = {
                'uid' : uid,
                'aid' : aid,
                'dall' : dall
            }
            return render(request,"myapp/add_course.html",context)

@auth
def view_course(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        call = Course.objects.all()     # fetch all records from the model
        context = {
            'uid' : uid,
            'aid' : aid,
            'call' : call
        }
        return render(request,"myapp/view_course.html",context)
    
@auth
def all_faculty(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        fall = Faculty.objects.all()     # fetch all records from the model
        context = {
            'uid' : uid,
            'aid' : aid,
            'fall' : fall
        }
        return render(request,"myapp/all_faculty.html",context)

@auth
def del_course(request,pk):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        try:
            
            course_id = Course.objects.get(id  = pk)
            course_id.delete() # for delete
            call = Course.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'call' : call
            }
            return render(request,"myapp/view_course.html",context)
        except:
            call = Course.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'call' : call
            }
            return render(request,"myapp/view_course.html",context)

@auth
def edit_course(request,pk):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
            
        course_id = Course.objects.get(id  = pk)
        
        context = {
            'uid' : uid,
            'aid' : aid,
            'course_id' : course_id
        }
        return render(request,"myapp/edit_course.html",context)
    
@auth
def update_course(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        cid = Course.objects.get(id = request.POST['cid'])
        dep = Department.objects.get(name = request.POST['department'])
        cid.department_id = dep
        cid.name = request.POST['course']
        cid.save()
        context = {
            'uid' : uid,
            'aid' : aid
        }
        return render(request,"myapp/edit_course.html",context)
    
@auth
def del_department(request,pk):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        try:
            
            department_id = Department.objects.get(id = pk)
            department_id.delete() # for delete
            dall = Department.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'dall' : dall
            }
            return render(request,"myapp/view_department.html",context)
        except:
            dall = Department.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'dall' : dall
            }
            return render(request,"myapp/view_department.html",context)
        
@auth
def edit_department(request,pk):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
            
        department_id = Department.objects.get(id  = pk)
        print("--------->>>> department idddd ",department_id)
        context = {
            'uid' : uid,
            'aid' : aid,
            'department_id' : department_id
        }
        return render(request,"myapp/edit_department.html",context)
    
@auth
def update_department(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        did = Department.objects.get(id = request.POST['did'])
        did.name = request.POST['department']
        did.save()

        dall = Department.objects.all() 
        context = {
            'uid' : uid,
            'aid' : aid,
            'dall' : dall
        } 
        return render(request,"myapp/view_department.html",context)
    
@auth
def del_faculty(request,pk):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        try:
            
            faculty_id = Faculty.objects.get(id  = pk)
            faculty_id.delete() # for delete
            fall = Faculty.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'fall' : fall
            }
            return render(request,"myapp/all_faculty.html",context)
        except:
            fall = Faculty.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'fall' : fall
            }
            return render(request,"myapp/all_faculty.html",context)
        
@auth
def add_student(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        if request.POST:
            aid = Admin.objects.get(user_id = uid)
            
            d_id = Department.objects.get(name = request.POST['department'])
            c_id = Course.objects.get(name = request.POST['course_selection'])
            f_id = Faculty.objects.get(firstname = request.POST['faculty_selection'])

            # print("==========>>>>>> d_id",d_id)
            # print("==========>>>>>> f_id",f_id)
            # print("==========>>>>>> c_id",c_id)

            email = request.POST['email']
            contact_no = request.POST['contact_no']
            firstname = request.POST['firstname']
            fathername = request.POST['fathername']
            lastname = request.POST['lastname']
            address = request.POST['address']
            qualification = request.POST['qualification']
            githublink = request.POST['githublink']
            instalink = request.POST['instalink']
            linkedinlink = request.POST['linkedinlink']

            a_pic = request.FILES['aadhar']
            pic = request.FILES['pic']

            li = ['sd45','ad45','45fd','ety4']
            password = email[3:5] + random.choice(li) + firstname[3:5] + contact_no[3:6]

            user_id = User.objects.create(email = email,
                                          password = password,
                                          role = "Student")
            
            sid = Student.objects.create(user_id = user_id,
                                         department_id = d_id,
                                         course_id = c_id,
                                         faculty_id = f_id,
                                         firstname = firstname,
                                         fathername = fathername,
                                         lastname = lastname,
                                         contact_no = contact_no,
                                         qualification = qualification,
                                         github_link = githublink,
                                         linked_id = linkedinlink,
                                         insta_id = instalink,
                                         address = address,
                                         aadhar = a_pic,
                                         pic = pic)
            
            # sall = Student.objects.all()

            s_msg = "Successfully Student added!!!"

            context = {
                'uid' : uid,
                'aid' : aid,
                # 'sall' : sall
                's_msg' : s_msg
            }
            return render(request,"myapp/add_student.html",context)
        else:
            aid = Admin.objects.get(user_id = uid)
            dall = Department.objects.all()
            fall = Faculty.objects.all()
            call = Course.objects.all()
            
            context = {
                'uid' : uid,
                'aid' : aid,
                'dall' : dall,
                'fall' : fall,
                'call' : call
            }
            return render(request,"myapp/add_student.html",context)
    
@auth
def all_student(request):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        sall = Student.objects.all()     # fetch all records from the model
        context = {
            'uid' : uid,
            'aid' : aid,
            'sall' : sall
        }
        return render(request,"myapp/all_student.html",context)

@auth
def del_student(request,pk):
    uid = User.objects.get(email = request.session['email'])
    if uid.role == 'Admin':
        aid = Admin.objects.get(user_id = uid)
        try:
            
            student_id = Student.objects.get(id  = pk)
            student_id.delete() # for delete
            sall = Student.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'sall' : sall
            }
            return render(request,"myapp/all_student.html",context)
        except:
            sall = Student.objects.all()     # fetch all records from the model
            context = {
                'uid' : uid,
                'aid' : aid,
                'sall' : sall
            }
            return render(request,"myapp/all_student.html",context)
        
def forgot_password(request):
    if request.POST:
        email = request.POST['email']
        try:
            uid = User.objects.get(email = email)

            if uid:

                otp =random.randint(1111,9999)

                uid.otp = otp

                uid.save()

                mySendMail("Forgot Password","myemailTemplate",email,{'otp' : otp})

                context = {
                    'email' : email
                }
                return render(request,"myapp/reset_password.html",context)
        
        except:
            context = {
                "e_msg" : "User Does not exists !!"
            }
            return render(request,"myapp/forgot_password.html",context)            
    else:
        return render(request,"myapp/forgot_password.html")
    
def reset_password(request):
    if request.POST:
        email = request.POST['email']
        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        repassword = request.POST['repassword']

        uid = User.objects.get(email = email)
        if str(uid.otp) == otp:
            if newpassword == repassword:
                uid.password = newpassword
                uid.save()
                context = {
                    "s_msg" : "Successfully Password reset !!"
                }
                return render(request,"myapp/login.html",context)
            else:
                context = {
                    "e_msg" : "Incorrect password - Does not match !!"
                }
                return render(request,"myapp/login.html",context)
        else:
            context = {
                    "e_msg" : "OTP Does not match !!"
            }
            return render(request,"myapp/login.html",context)