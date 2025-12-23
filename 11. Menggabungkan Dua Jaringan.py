network1 = ipaddress.ip_network('192.168.1.0/25')
network2 = ipaddress.ip_network('192.168.1.128/25')

combined_network = network1.supernet(new_prefix=24)
print("Jaringan yang digabungkan:", combined_network)
# Fungsi: Menggabungkan dua subnet menjadi satu.
# Kondisi: Ketika Anda ingin menyatukan dua jaringan yang berdekatan.
