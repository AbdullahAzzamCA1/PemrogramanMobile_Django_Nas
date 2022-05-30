from django.contrib import admin
from django.urls import path
from projectapp.views import *
from TheApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # App Helo
    path('salam/', greet, name='greet'),
    path('beranda/', beranda, name='beranda'),
    path('tentang/', tentang, name='tentang'),
    path('gallery/', gallery, name='gallery'),
    # TheApp
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('aboutus/', aboutus, name='aboutus'),
    path('login/', login, name='login'),
    path('divisi/', getDivisi, name='divisi'),
    path('jabatan/', getJabatan, name='jabatan'),
    path('pegawai/', getPegawai, name='pegawai'),
    path('pegawai/form', formPegawai, name='formPegawai'),
    path('pegawai/create', createPegawai, name='createPegawai'),
]
