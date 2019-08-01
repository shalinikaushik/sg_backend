# -*- coding: utf-8 -*-
from cvd_portal.models import Patient
from medicine_reminder.models import *
from medicine_reminder.serializers import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework.exceptions import ParseError
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from cvd_portal.fcm import send_message
from random import randint
import logging
logger = logging.getLogger(__name__)

# to get the list of medicines starting containing letter
class MedicineList(generics.ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

    def get(self, request):
        if request.GET.get('name','') == '':
            return super(MedicineList, self).get(self, request)
        else:
            try:
                mediData = Medicine.objects.all().filter(name_contains=request.GET.get('name', ''))
            except:
                return JsonResponse(
                    {"Error": "invalid"},
                    safe=False, content_type='application/json')
            return JsonResponse(
                MedicineSerializer(mediData).data,
                safe=False, content_type='application/json')

# to read data of single medicine
class MedicineCRUD(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Medicine.objects.all()
    serializer_class = MedicineDataSerializer

# CRUD data of particular reminder
class ReminderDataForParticularPatient(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ReminderDataForParticularMed.objects.all()
    serializer_class = ReminderForPatientSerializer

# CRUD Patient data
class PatientDataInChikitsa(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = PatientInChikitsaData.objects.all()
    serializer_class = PatientDataCRUDSerializer

# CRUD for doctor data
class DoctorDataInChikitsa(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = DoctorInChikitsaData.objects.all()
    serializer_class = DoctorDataCRUDSerializer

class ReminderDataForParticularPatientCreate(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = ReminderDataForParticularMed.objects.all()
    serializer_class = ReminderForPatientSerializer

# # CRUD for Notification
# class NotificationsData(generics.ListCreateAPIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = NotificationInChikitsa.objects.all()
#     serializer_class = NotificationListSerializer
#
#     def get(self, request):
#         if request.GET.get('notif','') == '':
#             return super(NotificationsData, self).get(self, request)
#             else:
#                 try:
#                     if request.GET.get('patientid',''):
#                         notifData = Notifications.objects.filter(notification_app = 2).filter(patient = request.GET.get('patientid',''))
#                     else if request.GET.get('doctorid',''):
#                         notifData = Notifications.objects.filter(notification_app = 2).filter(doctor = request.GET.get('doctorid',''))
#                 except:
#                     return JsonResponse(
#                         {"Error": "invalid"},
#                         safe=False, content_type='application/json')
#                 return JsonResponse(
#                     MedicineSerializer(mediData).data,
#                     safe=False, content_type='application/json')
