from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    otp = models.IntegerField(default=456)
    is_active = models.BooleanField(default=False)
    role = models.CharField(max_length=10) # student / faculty
    create_at = models.DateTimeField(auto_now_add=True,blank=False)

    def __str__(self):
        return self.email

class Admin(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=12)
    pic=models.FileField(upload_to='media/images/',default='media/mypic.png')

    def __str__(self):
        return self.firstname
    
class Department(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=12)
    pic=models.FileField(upload_to='media/images/',default='media/mypic.png')

    def __str__(self):
        return self.firstname 
    
class Course(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty_id = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    fathername = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=12)
    qualification = models.CharField(max_length=50,null=True, blank=True)
    github_link = models.CharField(max_length=100, null=True, blank=True)
    linked_id = models.CharField(max_length=100, null=True, blank=True)
    insta_id = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    aadhar=models. FileField(upload_to='media/images/')
    pic=models.FileField(upload_to='media/images/',default='media/s1.png')

    def __str__(self):
        return self.firstname
    
class Assignments(models.Model):
    title = models.ForeignKey(User,on_delete=models.CASCADE)
    a_file =models. FileField(upload_to='media/doc/')


class Accounts(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE) 
    date = models.DateField()
    amount = models.IntegerField(default=0000)
    status = models.CharField(default="PENDING")
    
    def _str_(self):
        return self.student_id.firstname +" : "+str(self.amount)
