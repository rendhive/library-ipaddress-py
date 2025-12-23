ip = ipaddress.ip_network('192.0.2.0/24', strict=False)

if not ip.is_private:
    print(f"{ip} adalah alamat jaringan publik.")
# Fungsi: Memastikan jaringan tidak termasuk dalam rentang alamat privat.
# Kondisi: Ketika Anda ingin memeriksa jika untuk penggunaan publik atau privat.
