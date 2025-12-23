network = ipaddress.ip_network('192.168.1.0/24')
new_network = network.supernet(new_prefix=20)
print("Subnet baru:", new_network)
# Fungsi: Mengubah subnet mask dari jaringan.
# Kondisi: Ketika Anda perlu mengubah pengaturan subnet dari jaringan yang ada.
