from fungsi import *

while True:
	cmd = input("Pilihan menu (A)dd,(L)ist,(S)earch,(D)elete,(Q)uit = ")

	if cmd == 'a'or cmd == 'A':
		tambah()

	elif cmd == 'l'or cmd == 'L':
		daftar()

	elif cmd == 's'or cmd == 'S':
		cari()

	elif cmd == 'd'or cmd == 'D':
		hapus()

	elif cmd == 'q' or cmd == 'Q':
		break
	
	else:
		print('Menu tidak terdaftar')
		
print('Terima Kasih~~~')
