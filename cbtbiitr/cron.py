import os
from django.core import management
from django.conf import settings
# from django_cron import CronJobBase, Schedule
#
# class Backup(CronJobBase):
#     RUN_AT_TIMES = ['6:00', '18:00']
#     schedule = Schedule(run_at_times=RUN_AT_TIMES)
#     code = 'cron.Backup'
#
#     def __init__(self):
#         # directory = settings.DBBACKUP_STORAGE_OPTIONS['/var/swasth-garbh']
#         # if not os.path.exists(directory):
#         #     os.makedirs(directory)
#         pass
#
#     def do(self):
#         management.call_command('dbbackup')

# def my_scheduled_job():
#     management.call_command('dbbackup')
