network = ipaddress.ip_network('192.168.1.0/24')
for host in network.hosts():
    print("Host dalam jaringan:", host)
# Fungsi: Mengiterasi semua host dalam jaringan berdasarkan notasi CIDR.
# Kondisi: Ketika Anda ingin mengidentifikasi semua alamat host dalam subnet.
