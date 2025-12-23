network = ipaddress.ip_network('192.168.1.0/30')

print("Alamat IP yang tersedia dalam jaringan:")
for ip in network.hosts():
    print(ip)
# Fungsi: Mengiterasi dan menampilkan semua alamat IP yang tersedia dalam subnet.
# Kondisi: Ketika Anda perlu mendapatkan semua alamat host yang dapat digunakan dalam jaringan.
