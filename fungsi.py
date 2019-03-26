from data import *

def tambah():
	nama = input("Nama Kontak : ")
	nomor = input("Nomor Kontak : ")
	contact [nama] = nomor

def hapus():
	hapus = input("Nama yang ingin di hapus : ")
	if hapus in contact.keys():
		del contact[hapus]
	else:
		print("Tidak ada kontak yang bernama : ", hapus)

def daftar():
	for nama, nomor in contact.items():
		print(nama,nomor)

def cari():
	cari = input("Nama yang mau di cari : ")
	no= contact.get(cari)
	if cari in contact.keys():
		print(cari , "nomor nya adalah " , no)
	else:
		print("Kontak tidak terdaftar")

