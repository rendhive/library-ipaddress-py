network = ipaddress.ip_network('192.168.0.0/24')
print("Jumlah host yang dapat digunakan:", network.num_addresses - 2)  # Kurangi 2 untuk alamat jaringan dan broadcast
# Fungsi: Menghitung jumlah alamat host yang dapat digunakan dalam jaringan.
# Kondisi: Ketika Anda ingin mengetahui jumlah alamat yang dapat dialokasikan untuk host.
