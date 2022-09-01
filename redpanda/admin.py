
from django.contrib import admin
from redpanda.models import Mesin, Unit, Feeder, Har, Cost

# Register your models here.
class MesinAdmin(admin.ModelAdmin):
    list_display = ('id','nama_unit_id','unit','nama_mesin','daya_mampu','is_sewa',)


class UnitAdmin(admin.ModelAdmin):
    list_display = ('id','nama_unit',)


class FeederAdmin(admin.ModelAdmin):
    list_display = ('id','tanggal','jam','kota','tona','kolongan','lesabe','tamako','mainlinepetta','pettakota','mainlinetahuna','kendahe','bowongkulu','kotatamako','lapango','tahuna','salurang','pintareng','tahunaincome')


class HarAdmin(admin.ModelAdmin):
    list_display = ('mesin_id','tanggal_jumat','jumat','sabtu','minggu','senin', 'selasa','rabu','kamis')


class CostAdmin(admin.ModelAdmin):
    list_display = ('id','mesin_id','tanggal','fix_cost','time_base_vcost','sfc_50','sfc_75','sfc_100','harga_sewa','pajak_air','susut_trafo','susut_jaringan')


admin.site.register(Mesin, MesinAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Feeder, FeederAdmin)
admin.site.register(Har, HarAdmin)
admin.site.register(Cost, CostAdmin)

