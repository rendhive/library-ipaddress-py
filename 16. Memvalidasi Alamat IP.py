try:
    valid_ip = ipaddress.ip_address('256.256.256.256')
except ValueError:
    print("Alamat IP tidak valid.")
# Fungsi: Memeriksa validitas alamat IP.
# Kondisi: Ketika Anda perlu memastikan alamat IP sesuai dengan standar yang berlaku.
