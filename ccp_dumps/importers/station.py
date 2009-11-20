#!/usr/bin/env python
"""
Import station related data.
"""
from apps.eve_db.models import *

def import_ramActivities(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from ramActivities'):
        imp_obj, created = ResearchAndMfgActivity.objects.get_or_create(id=row['activityID'])
        imp_obj.name = row['activityName']
        imp_obj.description = row['description']
        
        if row['iconNo']:
            imp_obj.icon_filename = row['iconNo']
        
        if row['published'] == 1:
            imp_obj.is_published = True
        else:
            imp_obj.is_published = False

        imp_obj.save()
    c.close()
    
def import_staServices(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from staServices'):
        imp_obj, created = StationService.objects.get_or_create(id=row['serviceID'])
        imp_obj.name = row['serviceName']
        imp_obj.description = row['description']
        imp_obj.save()
    c.close()