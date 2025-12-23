network = ipaddress.ip_network('192.168.1.0/24')
ip = ipaddress.ip_address('192.168.1.10')

if ip in network:
    print(f"{ip} berada dalam jaringan {network}.")
else:
    print(f"{ip} tidak berada dalam jaringan {network}.")
# Fungsi: Mengecek apakah suatu alamat IP ada di dalam jaringan.
# Kondisi: Ketika Anda ingin memverifikasi keanggotaan alamat IP dalam subnet.
