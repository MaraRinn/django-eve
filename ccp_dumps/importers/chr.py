#!/usr/bin/env python
"""
Import character data.

Tables imported:
chrRaces
"""
# Setup the Django environment if this is being executed directly.
if __name__ == "__main__":
    import os
    import sqlite3
    import constants
    constants.setup_environment()
from apps.eve_db.models import *

def import_chrRaces(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from chrRaces'):
        imp_obj, created = EVERace.objects.get_or_create(id=row['raceID'])
        imp_obj.name = row['raceName']
        imp_obj.short_description = row['shortDescription']
        imp_obj.description = row['description']
        
        graphic_id = row['graphicID']
        if graphic_id:
            imp_obj.graphic = EVEGraphic.objects.get(id=graphic_id)

        imp_obj.save()
    c.close()
    
def import_chrFactions(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from chrFactions'):
        imp_obj, created = Faction.objects.get_or_create(id=row['factionID'])
        imp_obj.name = row['factionName']
        imp_obj.description = row['description']
        
        if row['solarSystemID']:
            solar_system, ss_created = SolarSystem.objects.get_or_create(id=row['solarSystemID'])
            imp_obj.solar_system = solar_system
            
        if row['corporationID']:
            corp, corp_created = NPCCorporation.objects.get_or_create(id=row['corporationID'])
            imp_obj.corporation = corp
            
        imp_obj.size_factor = row['sizeFactor']
        imp_obj.station_count = row['stationCount']
        imp_obj.station_system_count = row['stationSystemCount']

        imp_obj.save()
    c.close()
    
def import_chrBloodlines(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from chrBloodlines'):
        imp_obj, created = Bloodline.objects.get_or_create(id=row['bloodlineID'])
        imp_obj.name = row['bloodlineName']
        imp_obj.race = EVERace.objects.get(id=row['raceID'])
        imp_obj.description = row['description']
        imp_obj.male_description = row['maleDescription']
        imp_obj.female_description = row['femaleDescription']
        starter_ship, ship_created = EVEInventoryType.objects.get_or_create(id=row['shipTypeID'])
        imp_obj.starter_ship_type = starter_ship
        imp_obj.starting_perception = row['perception']
        imp_obj.starting_willpower = row['willpower']
        imp_obj.starting_charisma = row['charisma']
        imp_obj.starting_memory = row['memory']
        imp_obj.starting_intelligence = row['intelligence']
        imp_obj.short_description = row['shortDescription']
        imp_obj.short_male_description = row['shortMaleDescription']
        imp_obj.short_female_description = row['shortFemaleDescription']
        if row['graphicID']:
            imp_obj.graphic = EVEGraphic.objects.get(id=row['graphicID'])
        imp_obj.save()
    c.close()
    
def import_chrAncestries(conn):
    c = conn.cursor()
    
    for row in c.execute('select * from chrAncestries'):
        imp_obj, created = Ancestry.objects.get_or_create(id=row['ancestryID'])
        imp_obj.name = row['ancestryName']
        imp_obj.bloodline = Bloodline.objects.get(id=row['bloodlineID'])
        imp_obj.description = row['description']
        imp_obj.perception_bonus = row['perception']
        imp_obj.willpower_bonus = row['willpower']
        imp_obj.charisma_bonus = row['charisma']
        imp_obj.memory_bonus = row['memory']
        imp_obj.intelligence_bonus = row['intelligence']
        imp_obj.short_description = row['shortDescription']
        if row['graphicID']:
            imp_obj.graphic = EVEGraphic.objects.get(id=row['graphicID'])
        imp_obj.save()
    c.close()

if __name__ == "__main__":
    conn = sqlite3.connect(constants.DB_FILE)
    conn.row_factory = sqlite3.Row
    
    import_chrRaces(conn)
    import_chrFactions(conn)
    import_chrBloodlines(conn)
    import_chrAncestries(conn)