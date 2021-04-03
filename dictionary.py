pelanggan = {
	"nama" : "Aldi",
	"umur" : "21"
}

pelanggan_2 = {
	"nama" : "Ipul",
	"umur" : "19"
}

daftar_pelanggan = []
daftar_pelanggan.append(pelanggan)
daftar_pelanggan.append(pelanggan_2)

for pelanggan in daftar_pelanggan:
	print("Nama : {}" . format(pelanggan["nama"]))
	print("Umur : {}" . format(pelanggan["umur"]))

#print(pelanggan["nama"])
#print(pelanggan_2["nama"])

#change dict value
#pelanggan_2["umur"] = 17

#print(pelanggan_2["nama"])
#print(pelanggan_2["umur"])

#loop in dictionary
#for x in pelanggan:
	#print(x) #print keys
	#print(pelanggan[x])
	#print(pelanggan_2[x])
