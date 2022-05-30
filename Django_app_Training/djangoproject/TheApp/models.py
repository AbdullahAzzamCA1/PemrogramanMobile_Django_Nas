from django.db import models


# Create your models here.

class Divisi(models.Model):
    nama = models.CharField(max_length=45)

    def __str__(self):
        return self.nama

class Jabatan(models.Model):
    nama = models.CharField(max_length=45)

    def __str__(self):
        return self.nama


class Pegawai(models.Model):
    nip = models.CharField(max_length=3)
    nama = models.CharField(max_length=45)
    gender = models.CharField(max_length=1)
    jabatan = models.ForeignKey(Jabatan, models.DO_NOTHING)
    divisi = models.ForeignKey(Divisi, models.DO_NOTHING)
    alamat = models.TextField()
    email = models.CharField(max_length=45)
    foto = models.FileField()

    def __str__(self):
        return self.nama