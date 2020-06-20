from django.db import models
from django.utils import timezone

# Create your models here.
SEMESTER_CHOICES = ( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ("6", "6"), 
    ("7", "7"), 
    ("8", "8"), 
) 
COURSE_CHOICES = ( 
    ("img", "IMG"),
    ("imt","IMT"),
    ("cse","CSE"),
    ("pgmba","PG-MBA") ,
    ("pgmtech","PG-MTech") ,
    ("phd","Phd")
) 
HOSTEL_CHOICES = (
    ("gh","Girls Hostel"),
    ("bh1","Boys Hostel 1"),
    ("bh2","Boys Hostel 2"),
    ("bh3","Boys Hostel 3"),
      
)


class Register(models.Model):
    register_id = models.AutoField
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=254)
    student_password = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=20)
    hostel = models.CharField( 
        max_length = 20, 
        choices =  HOSTEL_CHOICES,
        )
    image = models.ImageField(upload_to='student/images', default="")
    date_in = models.DateTimeField(auto_now_add=True)
    course = models.CharField( 
        max_length = 20, 
        choices = COURSE_CHOICES, 
        )
    gender = models.CharField( 
        max_length = 10, 
        choices = (("male","Male"),("female",("Female"))), 
        )
    hostel_floor = models.CharField(
        max_length = 20,
        choices = ( ("0","Ground Floor"),
        ("1","1st Floor"), ("2","2nd Floor"), ("3","3rd Floor") )
    )
    s_contact = models.CharField(max_length=9999999999)
    p_contact = models.CharField(max_length=9999999999)
    address = models.CharField(max_length=2000)
     


