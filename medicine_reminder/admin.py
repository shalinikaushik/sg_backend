from django.contrib import admin
from medicine_reminder.models import *
# Register your models here.
admin.site.register(Medicine)
admin.site.register(ReminderDataForParticularMed)
admin.site.register(PatientInChikitsaData)
admin.site.register(DoctorInChikitsaData)
