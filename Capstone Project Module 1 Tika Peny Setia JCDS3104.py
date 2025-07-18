"""
Judul: Prediksi Estimasi Waktu Pengiriman Barang Jasa Ekspedisi

Deskripsi:
Tugas ini dilakukan untuk memenuhi tugas capstone project module 1.

"""

from tabulate import tabulate

data_paket = [
    {
        "kode_unik": "PKT001",
        "asal": "Jakarta",
        "tujuan": "Bandung",
        "jarak (km)": 150,
        "jenis_layanan": "reguler",
        "estimasi_tiba": 3, 
        "status": "Dalam Perjalanan",
        "Biaya (Rp)": 30000
    },
    {
        "kode_unik": "PKT002",
        "asal": "Surabaya",
        "tujuan": "Yogyakarta",
        "jarak (km)": 325,
        "jenis_layanan": "ekspres",
        "estimasi_tiba": 2, 
        "status": "Dikirim",
        "Biaya (Rp)": 60000
    },
    {
        "kode_unik": "PKT003",
        "asal": "Medan",
        "tujuan": "Padang",
        "jarak (km)": 480,
        "jenis_layanan": "reguler",
        "estimasi_tiba": 4, 
        "status": "Paket telah sampai",
        "Biaya (Rp)": 50000
    },
    {
        "kode_unik": "PKT004",
        "asal": "Semarang",
        "tujuan": "Jakarta",
        "jarak (km)": 450,
        "jenis_layanan": "ekspres",
        "estimasi_tiba": 2, 
        "status": "Diproses",
        "Biaya (Rp)": 70000
    }
] 
kode_urut = 1

while True:
    print ("\n=== MENU PENGIRIMAN BARANG")
    print("1. Tambahkan Paket")
    print("2. Tampilkan Semua Data Paket")
    print("3. Ubah Paket")
    print("4. Hapus Paket")
    print("5. Cari Paket")
    print("6. Keluar")
    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        asal=input("Asal: ")
        tujuan=input("Tujuan: ")
        jarak=float(input("Jarak (km): "))
        jenis_layanan=input("Layanan(reguler/ekspres): ").lower()
    
        if jenis_layanan== "reguler":   #estimasi waktu
            estimasi=int(jarak/60)
            if jarak %60!=0:
                estimasi+=1
            biaya=int(jarak * 2000)
        elif jenis_layanan== "ekspres":
            estimasi=int(jarak/80)
            if jarak %80 !=0:
                estimasi+=1
            biaya=int(jarak * 3000)
        else:
            print("Layanan tidak valid.")
            continue

        status="Diproses"
        kode_unik= f"PKT{kode_urut:03}"
        kode_urut+=1

        data_paket.append({
            "Kode Unik": kode_unik,
            "Asal": asal,
            "Tujuan": tujuan,
            "Jarak (km)": jarak,
            "Layanan": jenis_layanan,
            "Estimasi (hari)": estimasi,
            "Status": status,
            "Biaya (Rp)": biaya
        })
        print("Paket berhasil ditambahkan.")

    elif menu == "2":
        if len(data_paket)== 0:
            print("Tidak ada data paket.")
        else:
            print("\n Daftar Paket:")
            print(tabulate(data_paket, headers="keys", tablefmt="grid"))

    elif menu == "3":
        kode=input("Masukkan kode unik yang ingin diubah: ")
        ditemukan=False
        for i in range(len(data_paket)):
            if data_paket[i]["kode_unik"]== kode:
                asal=input("Asal Baru: ")
                tujuan=input("Tujuan baru: ")
                jarak=float(input("Jarak (km) baru: "))
                jenis_layanan=input("Layanan baru(reguler/ekspres): ").lower()
                
                if jenis_layanan== "reguler":
                    estimasi=int(jarak/60)
                    if jarak %60!=0:
                        estimasi+=1
                    biaya=int(jarak * 2000)
                elif jenis_layanan== "ekspres":
                    estimasi=int(jarak/80)
                    if jarak %80 !=0:
                        estimasi+=1
                    biaya=int(jarak * 3000)
                else:
                    print("Layanan tidak valid.")
                    break

                status="Diproses"
                data_paket[i]={
                    "Kode Unik": kode,
                    "Asal": asal,
                    "Tujuan": tujuan,
                    "Jarak (km)": jarak,
                    "Layanan": jenis_layanan,
                    "Estimasi (hari)": estimasi,
                    "Status": status,
                    "Biaya (Rp)": biaya
                }
                ditemukan=True
                print("Data berhasil diubah.")
                break

        if not ditemukan:
            print("Kode tidak ditemukan.")

    elif menu== "4":
        kode=input("Masukkan kode unik yang ingin dihapus: ")
        indeks=-1
        for i in range(len(data_paket)):
            if data_paket[i]["kode_unik"]== kode:
                indeks=i
                break
        if indeks!=-1:
            del data_paket[indeks]
            print("Data berhasil dihapus.")
        else:
            print("Kode tidak ditemukan.")

    elif menu== "5":
        kode=input("Masukkan kode unik yang dicari: ")
        ditemukan=False
        for i in range(len(data_paket)):
            if data_paket[i]["kode_unik"]== kode:
                print("Data ditemukan:")
                print(tabulate([data_paket[i]], headers="keys", tablefmt="grid"))
                ditemukan=True
                break
        if not ditemukan:
            print("Data tidak ditemukan.")

    elif menu== "6":
        print("Terimakasih, program selesai.")
        break
    else:
        print("Pilihan tidak valid.")