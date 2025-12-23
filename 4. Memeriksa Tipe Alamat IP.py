ip = ipaddress.ip_address('10.0.0.1')

if ip.version == 4:
    print("Ini adalah alamat IPv4.")
else:
    print("Ini adalah alamat IPv6.")
# Fungsi: Memeriksa versi dari alamat IP (IPv4 atau IPv6).
# Kondisi: Ketika Anda perlu membedakan antara alamat IPv4 dan IPv6.
