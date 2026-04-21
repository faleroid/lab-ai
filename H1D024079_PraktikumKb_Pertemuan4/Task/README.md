# Sistem Pakar Diagnosa Kerusakan Hardware Komputer (Python)

Sistem pakar sederhana berbasis Python yang dirancang untuk membantu pengguna mengidentifikasi kerusakan pada perangkat keras (hardware) komputer berdasarkan gejala yang dialami. Program ini menggunakan metode **Inference Engine** sederhana dengan pendekatan *Forward Chaining* untuk mencocokkan gejala dengan basis pengetahuan.

## 🚀 Fitur Utama
- **Knowledge Base Berbasis Dictionary:** Aturan kerusakan disimpan dalam struktur data dictionary yang rapi, sehingga mudah untuk ditambah atau dimodifikasi.
- **Inference Engine Dinamis:** Menggunakan fungsi logika untuk mencocokkan gejala pengguna dengan aturan yang ada secara otomatis.
- **Solusi Langsung:** Memberikan rekomendasi perbaikan singkat untuk setiap kerusakan yang terdeteksi.
- **Penanganan Kondisi Tidak Terdeteksi:** Memberikan pesan informatif jika gejala yang dimasukkan tidak cocok dengan aturan mana pun.

## 🛠️ Daftar Kerusakan yang Didukung
Program ini dapat mendeteksi 5 jenis kerusakan umum:
1. **RAM Rusak:** Masalah pada modul memori.
2. **Power Supply (PSU) Lemah:** Masalah pada distribusi daya.
3. **Overheat (Prosesor):** Masalah suhu berlebih pada CPU.
4. **VGA Bermasalah:** Gangguan pada output visual/grafis.
5. **Hardisk Corrupt:** Masalah pada media penyimpanan data.

## 📋 Alur Kerja Sistem
Sistem bekerja dengan cara menanyakan serangkaian gejala kepada pengguna. Jika jawaban pengguna sesuai dengan **seluruh** syarat gejala dari suatu jenis kerusakan, sistem akan mengeluarkan diagnosa beserta solusinya.



## 💻 Cara Menjalankan
1. Pastikan Anda sudah menginstal **Python 3.x** di komputer Anda.
2. Simpan kode program ke dalam file, misalnya `diagnosa_pc.py`.
3. Jalankan melalui terminal atau command prompt:
   ```bash
   python diagnosa_pc.py