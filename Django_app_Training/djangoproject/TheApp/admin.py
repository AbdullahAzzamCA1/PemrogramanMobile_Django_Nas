from django.contrib import admin
from . models import Divisi, Pegawai, Jabatan

# Register your models here.
admin.site.register(Divisi)
admin.site.register(Jabatan)
admin.site.register(Pegawai)

