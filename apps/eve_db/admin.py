from django.contrib import admin
from apps.eve_db.models import *

class EVEInventoryCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_published')
admin.site.register(EVEInventoryCategory, EVEInventoryCategoryAdmin)

class EVEInventoryGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEInventoryGroup, EVEInventoryGroupAdmin)

class EVEInventoryTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'market_group', 'description')
admin.site.register(EVEInventoryType, EVEInventoryTypeAdmin)

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
 
class EVEAttributeCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
admin.site.register(EVEAttributeCategory, EVEAttributeCategoryAdmin)
 
class EVEAttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
admin.site.register(EVEAttributeType, EVEAttributeTypeAdmin)
 
class EVEInventoryTypeAttributesAdmin(admin.ModelAdmin):
    list_display = ('inventory_type', 'attribute', 'value_int', 'value_float')
admin.site.register(EVEInventoryTypeAttributes, EVEInventoryTypeAttributesAdmin)

class EVEGraphicAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name', 'icon_filename')
admin.site.register(EVEGraphic, EVEGraphicAdmin)

class EVERaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_description')
admin.site.register(EVERace, EVERaceAdmin)

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
