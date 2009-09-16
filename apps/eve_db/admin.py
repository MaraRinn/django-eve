"""
Admin interface models. Automatically detected by admin.autodiscover().
"""
from django.contrib import admin
from apps.eve_db.models import *

class EVEInventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_published')
admin.site.register(EVEInventoryCategory, EVEInventoryCategoryAdmin)

class EVEInventoryMetaGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'graphic')
admin.site.register(EVEInventoryMetaGroup, EVEInventoryMetaGroupAdmin)

class EVEInventoryMetaTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'parent_type', 'meta_group')
admin.site.register(EVEInventoryMetaType, EVEInventoryMetaTypeAdmin)

class EVEInventoryGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEInventoryGroup, EVEInventoryGroupAdmin)

class EVEInventoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'market_group', 'description')
admin.site.register(EVEInventoryType, EVEInventoryTypeAdmin)

class EVEInventoryFlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'type_text', 'order')
admin.site.register(EVEInventoryFlag, EVEInventoryFlagAdmin)

class EVEInventoryEffectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'is_offensive',
                    'is_assistance', 'is_published')
admin.site.register(EVEInventoryEffect, EVEInventoryEffectAdmin)

class EVEInventoryTypeEffectAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'effect', 'is_default')
admin.site.register(EVEInventoryTypeEffect, EVEInventoryTypeEffectAdmin)

class EVEInventoryTypeReactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'reaction_type', 'type', 'input')
admin.site.register(EVEInventoryTypeReactions, EVEInventoryTypeReactionsAdmin)

class EVEPOSResourcePurposeAdmin(admin.ModelAdmin):
    list_display = ('id', 'purpose')
admin.site.register(EVEPOSResourcePurpose, EVEPOSResourcePurposeAdmin)

class EVEPOSResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'control_tower_type', 'resource_type', 'purpose',
                    'quantity', 'faction')
admin.site.register(EVEPOSResource, EVEPOSResourceAdmin)

class ContrabandTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'faction', 'standing_loss', 
                    'confiscate_min_sec', 'attack_min_sec', 'fine_by_value')
admin.site.register(ContrabandType, ContrabandTypeAdmin)

class EVEInventoryBlueprintTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'blueprint_type', 'product_type', 'tech_level')
admin.site.register(EVEInventoryBlueprintType, EVEInventoryBlueprintTypeAdmin)

class EVEResearchMfgActivitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'icon_filename', 'is_published')
admin.site.register(EVEResearchMfgActivities, EVEResearchMfgActivitiesAdmin)

class EVETypeActivityMaterialsAdmin(admin.ModelAdmin):
    list_display = ('blueprint_type', 'activity', 'required_type', 'quantity')
admin.site.register(EVETypeActivityMaterials, EVETypeActivityMaterialsAdmin)    
 
class EVEUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_name', 'description')
admin.site.register(EVEUnit, EVEUnitAdmin)

class UniverseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(Universe, UniverseAdmin)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction')
admin.site.register(Region, RegionAdmin)

class FactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'solar_system')
admin.site.register(Faction, FactionAdmin)

class ConstellationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction', 'alliance')
admin.site.register(Constellation, ConstellationAdmin)

class SolarSystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'constellation', 'region', 'faction', 
                    'alliance', 'security_class', 'security_level')
admin.site.register(SolarSystem, SolarSystemAdmin)
 
class EVEInventoryAttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(EVEInventoryAttributeCategory, EVEInventoryAttributeCategoryAdmin)
 
class EVEInventoryAttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEInventoryAttributeType, EVEInventoryAttributeTypeAdmin)
 
class EVEInventoryTypeAttributesAdmin(admin.ModelAdmin):
    list_display = ('inventory_type', 'attribute', 'value_int', 'value_float')
admin.site.register(EVEInventoryTypeAttributes, EVEInventoryTypeAttributesAdmin)

class EVEGraphicAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name', 'icon_filename')
admin.site.register(EVEGraphic, EVEGraphicAdmin)

class EVEInventoryNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'group', 'type')
admin.site.register(EVEInventoryName, EVEInventoryNameAdmin)

class EVERaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description')
admin.site.register(EVERace, EVERaceAdmin)

class CorporateActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(CorporateActivity, CorporateActivityAdmin)

class NPCCorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'faction', 'description', 'station_count', 
                    'size', 'extent')
admin.site.register(NPCCorporation, NPCCorporationAdmin)

class EVEPlayerCorporationInline(admin.TabularInline):
    model = EVEPlayerCorporation
    fields = ('name', 'ticker')
    extra = 0

class EVEPlayerAllianceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ticker', 'member_count', 'date_founded')
    search_fields = ['name', 'ticker']
    date_hierarchy = 'date_founded'
    inlines = [EVEPlayerCorporationInline]
admin.site.register(EVEPlayerAlliance, EVEPlayerAllianceAdmin)

class EVEPlayerCorporationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ticker', 'member_count', 'alliance')
    search_fields = ['name', 'ticker']
admin.site.register(EVEPlayerCorporation, EVEPlayerCorporationAdmin)
