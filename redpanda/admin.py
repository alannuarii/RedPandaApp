
from django.contrib import admin
from redpanda.models import Mesin, Unit, Feeder

# Register your models here.
class MesinAdmin(admin.ModelAdmin):
    list_display = ('id','nama_unit_id','unit','nama_mesin','daya_mampu','is_sewa',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('id','nama_unit',)


class FeederAdmin(admin.ModelAdmin):
    list_display = ('id','tanggal','jam','kota','tona','kolongan','lesabe','tamako','mainlinepetta','pettakota','mainlinetahuna','kendahe','bowongkulu','kotatamako','lapango','tahuna','salurang','pintareng','tahunaincome')


admin.site.register(Mesin, MesinAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Feeder, FeederAdmin)

