from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        null=True, upload_to="", blank=True)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=15)
    forgot_pass_token = models.CharField(null=True, max_length=40)

    def __str__(self):
        return self.user.username


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    mobile = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=15)
    specialization = models.CharField(max_length=15)
    forgot_pass_token = models.CharField(null=True, max_length=40)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    app_id = models.CharField(primary_key=True, max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    mode = models.CharField(max_length=10)
