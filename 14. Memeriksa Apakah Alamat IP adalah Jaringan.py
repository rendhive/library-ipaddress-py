ip = ipaddress.ip_address('192.168.1.0')

if ip.is_loopback:
    print(f"{ip} adalah alamat loopback.")
elif ip.is_private:
    print(f"{ip} adalah alamat privat.")
else:
    print(f"{ip} adalah alamat publik.")
# Fungsi: Memeriksa tipe dari alamat IP.
# Kondisi: Ketika Anda perlu menentukan apakah alamat tersebut publik, privat, atau loopback.
