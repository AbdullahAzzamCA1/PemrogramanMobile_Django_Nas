from django.shortcuts import redirect, render
from .models import *
from TheApp.functions.functions import handle_uploaded_file
# from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def getDivisi(request):
    divisi_list = Divisi.objects.all()
    template = 'divisi.html'
    context = {
        'divisi_list':divisi_list
    }
    return render(request, template, context)

def getJabatan(request):
    jabatan_list = Jabatan.objects.all()
    template = 'jabatan.html'
    context = {
        'jabatan_list':jabatan_list
    }
    return render(request, template, context)

def getPegawai(request):
    pegawai_list = Pegawai.objects.all()
    template = 'pegawai.html'
    context = {
        'pegawai_list':pegawai_list
    }
    return render(request, template, context)

def formPegawai(request):
    ar_jabatan = Jabatan.objects.all()
    ar_divisi = Divisi.objects.all()
    template = 'form_pegawai.html'
    context = {
        'ar_jabatan':ar_jabatan,
        'ar_divisi':ar_divisi,
    }
    return render(request, template, context)

# @csrf_exempt
def createPegawai(request):
    if request.FILES:
        handle_uploaded_file(request.FILES['foto'])
    
    nip = request.POST['nip']
    nama = request.POST['nama']
    gender = request.POST['gender']
    jabatan = request.POST['jabatan']
    divisi = request.POST['divisi']
    alamat = request.POST['alamat']
    foto = request.FILES['foto']

    p = Pegawai()
    p.nip = nip
    p.nama = nama
    p.gender = gender
    p.jabatan_id = jabatan
    p.divisi_id = divisi
    p.alamat = alamat
    p.foto = foto
    p.save()

    pegawai_list =  Pegawai.objects.order_by('id')
    template = 'pegawai.html'
    context = {
        'pegawai_list' : pegawai_list
    }

    return redirect('/pegawai/')