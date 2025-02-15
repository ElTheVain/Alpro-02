def hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu):
    gaji_per_minggu = gaji_per_jam * jam_kerja_per_minggu  
    pendapatan_budi = gaji_per_minggu
    pendapatan_bersih = pendapatan_budi * 0.86
    uang_baju_aksesoris = pendapatan_bersih * 0.10
    uang_alat_tulis = pendapatan_bersih * 0.01
    sisa_uang = pendapatan_bersih - uang_baju_aksesoris - uang_alat_tulis
    uang_sedekah = sisa_uang * 0.25
    uang_anak_yatim = uang_sedekah * 0.30
    uang_kaum_dhuafa = sisa_uang - uang_anak_yatim
    print(f"pendapatan sebelum pajak: Rp{pendapatan_budi:,.0f}")
    print(f"pendapatan setelah pajak: Rp{pendapatan_bersih:,.0f}")
    print(f"uang baju dan aksesoris: Rp{uang_baju_aksesoris:,.0f}")
    print(f"pengeluaran uang alat tulis: Rp{uang_alat_tulis:,.0f}")
    print(f"jumlah uang sedekah: Rp{uang_sedekah:,.0f}")
    print(f"uang yang diterima anak yatim: Rp{uang_anak_yatim:,.0f}")
    print(f"uang yang diterima kaum dhuafa: Rp{uang_kaum_dhuafa:,.0f}")
gaji_per_jam = float(input("Gaji yang diinginkan Budi per jam: Rp"))
jam_kerja_per_minggu = int(input("Jumlah jam kerja per minggu: "))
hitung_pendapatan(gaji_per_jam, jam_kerja_per_minggu)
