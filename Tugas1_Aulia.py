def totHarga_tiket(umur, hari):
    # Harga Tiket Dasar
    harga = 100000

    # Jika umur penonton < 12 tahun atau > 60 tahun, diskon 50%
    if umur < 12 or umur > 60:
        harga *= 0.5

    # Jika penonton berusia antara 12 - 60 tahun dan membeli tiket pada hari kerja, mendapat diskon 5000
    elif hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jum'at"]:
        harga -= 10000

    # Jika pembelian tiket di akhir pekan (Sabtu/Minggu), tambahan biaya 10.000
    if hari in ["Sabtu", "Minggu"]:
        harga += 25000

    return int(harga)  # Pastikan mengembalikan nilai di semua kondisi


umur = int(input("Umur : "))
hari = input("Hari pembelian tiket : ")
tot_Harga = totHarga_tiket(umur, hari)
print(f"Total Harga : Rp {tot_Harga:,}")
