ip = ipaddress.ip_address('192.168.1.10')
network = ipaddress.ip_network('192.168.1.0/24')

print("Jaringan untuk alamat IP:", ip in network)
# Fungsi: Memverifikasi apakah suatu alamat IP berada dalam jaringan tertentu.
# Kondisi: Ketika Anda membutuhkan informasi jaringan dari alamat IP tersebut.
