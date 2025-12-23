network = ipaddress.ip_network('192.168.1.0/24')

print("Informasi jaringan:", network)
print("Alamat jaringan:", network.network_address)
print("Alamat broadcast:", network.broadcast_address)
# Fungsi: Mengambil informasi dasar dari objek jaringan.
# Kondisi: Ketika Anda perlu mendapatkan detail tentang jaringan tertentu.
