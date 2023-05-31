from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
    )

TIME_CHOICES = (
    ("7 AM", "7 AM"),
    ("8 AM", "8 AM"),
    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
)

GENDER_CHOICES = (
    ('M','M'),
    ('F','F'),
    ('O','O'),
)

SWIM_CHOICES = (
    ('Y','Y'),
    ('N','N'),
)

HOSTEL_CHOICES = (
    ('Satpura','Satpura'),
    ('Day Scholar','Day Scholar'),
    ('Shivalik','Shivalik'),
    ('Jwalamukhi','Jwalamukhi'),
    ('Aravali','Aravali'),
    ('Karakoram','Karakoram'),
    ('Nilgiri','Nilgiri'),
    ('Vindhyachal','Vindhyachal'),
    ('Kumaon','Kumaon'),
    ('Girnar','Girnar'),
    ('Udaigiri','Udaigiri'),
    ('Zanskar','Zanskar'),
    ('Kailash','Kailash'),
    ('Himadri','Himadri'),
    ('Sahyadri','Sahyadri'),
    ('Nalanda','Nalanda'),
)

DEPT_CHOICES = (
    ('CSE','CSE'),
    ('MT','MT'),
    ('BB','BB'),
    ('EE','EE'),
    ('AM','AM'),
    ('TT','TT'),
    ('MSE','MSE'),
    ('CH','CH'),
    ('SCAI','SCAI'),
)
# TIME_CHOICES = (
#     ("7 AM", "7 AM"),
#     ("3:30 PM", "3:30 PM"),
#     ("4 PM", "4 PM"),
#     ("4:30 PM", "4:30 PM"),
#     ("5 PM", "5 PM"),
#     ("5:30 PM", "5:30 PM"),
#     ("6 PM", "6 PM"),
#     ("6:30 PM", "6:30 PM"),
#     ("7 PM", "7 PM"),
#     ("7:30 PM", "7:30 PM"),
# )

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"

class studentuserdata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    guardianfirstname=models.CharField(max_length=100)
    guardianlastname=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobilenumber=models.CharField(max_length=13)
    entrynumber=models.CharField(max_length=12)
    department=models.CharField(max_length=6, choices=DEPT_CHOICES)
    hostel=models.CharField(max_length=20, choices=HOSTEL_CHOICES)
    roomnumber=models.CharField(max_length=10)
    emergencynumber=models.CharField(max_length=13)
    address=models.CharField(max_length=300)
    swim=models.CharField(max_length=1, choices=SWIM_CHOICES)
    slot1=models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    slot2=models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
