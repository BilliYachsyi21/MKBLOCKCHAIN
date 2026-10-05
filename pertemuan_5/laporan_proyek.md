# Laporan : Blockchain for Halal Coffee Supply Chain

Nama : Moh. Ni’am Billi Yachsyi

NIM : 2530801024

Kelas : INF-3D

## 1. Pendahuluan

Proyek **Blockchain for Halal Coffee Supply Chain** adalah aplikasi berbasis web yang dibangun menggunakan framework **Streamlit** dan modul inti berbasis Python (`core.py`). Aplikasi ini dirancang untuk mendemonstrasikan bagaimana teknologi *blockchain* dapat diterapkan guna memastikan transparansi, ketertelusuran (*traceability*), serta keabsahan data dalam rantai pasok kopi, mulai dari petani di perkebunan hingga proses pemesanan oleh konsumen akhir.

## 2. Arsitektur dan Komponen Sistem

Sistem ini terdiri dari dua file utama yang saling terintegrasi:

### A. Modul Inti (`core.py`)

Modul ini bertanggung jawab atas struktur data dasar dan logika kriptografi *blockchain*:

* **Kelas `Block`**:

  * Menyimpan atribut penting seperti `index`, `timestamp`, `data`, `previous_hash`, `nonce`, dan `hash`.

  * Memiliki fungsi `calculate_hash()` yang memanfaatkan algoritma **SHA-256** untuk mengenkripsi gabungan atribut blok.

  * Menerapkan mekanisme *Proof-of-Work* melalui fungsi `mine_block(difficulty)` yang memastikan *hash* memenuhi tingkat kesulitan tertentu (diawali sejumlah karakter `0`).

* **Kelas `Blockchain`**:

  * Mengelola rantai blok (*chain*), dimulai dari *Genesis Block* pada indeks ke-0.

  * Mengatur tingkat kesulitan (*difficulty*) penambangan (diset ke nilai `3` secara default).

  * Memiliki fungsi `add_block()` untuk menautkan blok baru ke blok terakhir dan melakukan penambangan.

  * Memiliki fungsi `is_chain_valid()` untuk memvalidasi integritas rantai secara keseluruhan guna mendeteksi adanya manipulasi data.

### B. Antarmuka Pengguna (`app.py`)

Antarmuka dibangun dengan **Streamlit** untuk menyajikan pengalaman interaktif:

* **Form Input Sidebar**: Memungkinkan pengguna memasukkan data pemesanan (nama pemesan, produk kopi, jumlah, pelengkap) serta data hulu rantai pasok (nama petani/aktor, jumlah panen dalam Kg, dan lokasi kebun).

* **Proses Mining**: Ketika tombol *Mine Block* ditekan, data digabungkan menjadi *payload* string, dibungkus dalam blok baru, ditambang secara otomatis, lalu dimasukkan ke dalam rantai dengan metrik waktu eksekusi yang tercatat.

* **Simulasi Serangan (Tampering)**: Fitur uji coba untuk mengubah data pada Blok #1 secara paksa guna menguji ketahanan sistem terhadap manipulasi.

* **Pemeriksaan Integritas**: Tombol verifikasi untuk memeriksa apakah rantai masih valid atau telah disusupi.

* **Blockchain Ledger Explorer**: Menampilkan daftar blok secara transparan melalui komponen *expander*, lengkap dengan rincian *payload*, *timestamp*, *nonce*, *hash* saat ini, dan *hash* sebelumnya.

## 3. Fitur Utama Aplikasi

1. **Katalog Produk Kopi & Pelengkap**: Menyediakan pilihan produk kopi populer (seperti Kopi Arabika Gayo, Robusta Temanggung, dll.) beserta opsi pelengkap dan kalkulasi harga otomatis dalam format Rupiah.

2. **Keamanan Kriptografi SHA-256**: Setiap perubahan sekecil apa pun pada data blok akan mengubah nilai *hash* secara drastis, sehingga melanggar tautan *pointer* ke blok berikutnya.

3. **Visualisasi Kesulitan & Performa**: Menampilkan *difficulty*, *target hash* (`000...`), serta durasi waktu yang dibutuhkan untuk proses *mining*.

## 4. Kesimpulan

Aplikasi **Blockchain for Halal Coffee Supply Chain** ini berhasil menunjukkan implementasi konsep dasar *blockchain* (desentralisasi semu, immutability, dan *proof-of-work*) ke dalam studi kasus nyata di industri agrikultur dan makanan. Sistem ini efektif dalam memastikan bahwa rekam jejak kopi dari hulu ke hilir tetap transparan dan terlindungi dari pemalsuan data.