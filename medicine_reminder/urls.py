from django.conf.urls import url, include
from rest_framework.authtoken import views
from medicine_reminder.views import *

app_name = 'medicine_reminder'

urlpatterns = [
    url(r'medicines',MedicineList.as_view()),
    url(r'medicine/data/(?P<pk>[0-9]+)$',MedicineCRUD.as_view()),
    url(r'reminder/data/(?P<pk>[0-9]+)$',ReminderDataForParticularPatient.as_view()),
    url(r'patient/(?P<pk>[0-9]+)$',PatientDataInChikitsa.as_view()),
    url(r'doctor/(?P<pk>[0-9]+)$',DoctorDataInChikitsa.as_view()),
    url(r'remindernew/(?P<pk>[0-9]+)$',ReminderDataForParticularPatientCreate.as_view()),
]
