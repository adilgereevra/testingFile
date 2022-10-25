from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from tables.models import Model2, Trends,Events,Scenario
# Register your models here.

@admin.register(Model2)
class Model2Admin(admin.ModelAdmin):
    pass

@admin.register(Trends)
class TrendsAdmin(admin.ModelAdmin):
    pass

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass

@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    pass