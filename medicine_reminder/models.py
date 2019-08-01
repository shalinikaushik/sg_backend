# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil import tz
from cvd_portal.models import *

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    medicine_Image = models.TextField()
    compunds = models.TextField()

class ReminderDataForParticularMed(models.Model):
    # meed to check the medicine_id how to map it uniquel
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True, blank=True)
    number_of_times_to_take_day = models.PositiveIntegerField(default=1)
    number_of_times_to_take_week = models.PositiveIntegerField(default=1)
    times = models.PositiveIntegerField(default=1 , null=True)
    extra_comments = models.CharField(max_length=100 , null=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medRemData')
    start_time = CustomDateTimeField(default=datetime.datetime.now)
    time_gap = models.DecimalField(max_digits = 2, decimal_places = 1)

class PatientInChikitsaData(models.Model):
    problems_faced = models.TextField()
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patientInChikitsaData')
    next_visit = CustomDateTimeField(default=datetime.datetime.now)
    doctor_comments = models.TextField()

class DoctorInChikitsaData(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctorInChikitsaData')
