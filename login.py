nama ="admin"
sandi = "12345"
lagi = 'y'
a=0
while lagi == 'y':
	username = str(input('Masukkan Username: '))
	password = str(input('Masukkan Password : '))
	if username == nama and password == sandi:
		print("Login sukses!")
		break
	elif username == nama or password== sandi:
		print("Username/Password tidak valid!")
	else:
		print("Password salah!")

	a = a+1
	if a == 3:
		print ("Sudah 3x input. Silahkan coba lagi nanti")
		break
	print()
	lagi=str(input("Input username dan sandi lagi? y/t:"))
	print()
