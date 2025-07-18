# Capstone-Project-Modul-1
Project Capstone Modul 1 Tika Peny Setia JCDS3104

📦 Estimasi Pengiriman Paket – Program CRUD Python
Program estimasi pengiriman paket adalah aplikasi berbasis Python yang dirancang untuk membantu pencatatan dan pemantauan pengiriman barang.
Program ini dibuat menggunakan prinsip CRUD agar pengguna dapat mengelola data pengiriman secara otomatis dan efisien.

🎯 Tujuan Program
1. Menampilkan data dalam format tabel dengan bantuan 'tabulate'.
2. Memberikan kode unik untuk setiap paket.
3. Menghitung estimasi waktu pengiriman berdasarkan jarak dan jenis
   layanan.
4. Menampilkan status pengiriman, seperti 'Diproses', 'Dikirim', 'Tiba di tujuan'.
5. Menghitung biaya pengiriman secara otomatis.

Pembuatan program ini cocok untuk:
1. Praktik pemrograman Python pemula.
2. Simulasi sistem logistik kecil.
3. Dasar pengembangan aplikasi pelacakan pengiriman.

 🔧 Fitur Utama
 1. Create (Tambah Data)
    - Input: asal, tujuan, jarak, jenis layanan.
    - Output: estimasi hari, biaya, status awasl, kode unik.
 2. Read (Lihat Data)
    - Mencari paket dengan kode unik.
    - Menampilkan semua data pengiriman dalam tabel.
 3. Update (Ubah Data)
    Mengubah data paket berdasarkan kode unik, memperbarui estimasi dan
    status otomatis.
 4. Delete (Hapus Data)
    Menghapus data berdasarkan kode unik paket.
 5. Estimasi dan Status
    - Estimasi waktu berdasarkan:
      a. Reguler: 60 km/h + 1 hari tambahan
      b. Ekspres: 80 km/h
    - Biaya pengiriman:
      a. Reguler: Rp 2000/km
      b. Ekspres: Rp 3000/km
    - Status otomatis berdasarkan estimasi:
      a. Hari ke-1: 'Diproses'
      b. Hari di tengah: 'Dikirim'
      c. Hari terakhir: 'Tiba di tujuan'
