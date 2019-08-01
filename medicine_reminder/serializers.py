from rest_framework import serializers
from medicine_reminder.models import *
from cvd_portal.serializers import DynamicFieldsModelSerializer,PatientSerializer1
from django.contrib.auth.models import User

# to get the list of medicines starting containing letter
class MedicineSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'pk',
            'name',
            'compunds'
        ]
# to read data of single medicine
class MedicineDataSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'pk',
            'name',
            'compunds',
            'medicine_Image'
        ]
# CRUD data of particular reminder
class ReminderForPatientSerializer(DynamicFieldsModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all())
    medicine_detail = serializers.SerializerMethodField('getMedicinesData')
    class Meta:
        model = ReminderDataForParticularMed
        fields = [
            'pk',
            'medicine_detail',
            'number_of_times_to_take_day',
            'number_of_times_to_take_week',
            'patient_id',
            'start_time',
            'time_gap',
            'times',
            'extra_comments'
        ]

    def getMedicinesData(self, obj):
        qset = Medicine.objects.all().filter(pk = obj.medicine_id)
        ser = MedicineSerializer(qset, many=True ,read_only = True)
        return ser.data


# CRUD Patient data
class PatientDataCRUDSerializer(DynamicFieldsModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all())
    all_medicines = serializers.SerializerMethodField('getAllMedicinesData')
    class Meta:
        model = PatientInChikitsaData
        fields = [
            'pk',
            'patient_id',
            'next_visit',
            'doctor_comments',
            'problems_faced',
            'all_medicines'
        ]

    def getAllMedicinesData(self, obj):
        q2set = Medicine.objects.all().filter(reminderdataforparticularmed__patient_id = obj.patient_id).distinct()
        ser = MedicineSerializer(q2set, many=True ,read_only = True)
        return ser.data

# CRUD for doctor data
class DoctorDataCRUDSerializer(DynamicFieldsModelSerializer):
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all())
    patients = serializers.SerializerMethodField('getPatientsData')
    class Meta:
        model = DoctorInChikitsaData
        fields = [
            'pk',
            'doctor_id',
            'patients',
        ]
    def getPatientsData(self, obj):
        qset = Patient.objects.filter(doctor_id = obj.pk)
        ser = PatientSerializer1(qset , many = True , read_only = True)
        return ser.data
