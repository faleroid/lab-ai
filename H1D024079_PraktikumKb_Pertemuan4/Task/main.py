gejala_pengguna = []

basis_pengetahuan = {
    "RAM Rusak": {
        "gejala": ["bunyi_beep", "layar_blank"],
        "solusi": "Coba lepas RAM, bersihkan pin kuningnya dengan penghapus pensil secara searah, lalu pasang kembali dengan rapat."
    },
    "Power Supply (PSU) Lemah": {
        "gejala": ["sering_restart", "mati_saat_beban_berat"],
        "solusi": "Periksa apakah ada komponen yang berbau hangus. Jika daya listrik tidak stabil, pertimbangkan untuk mengganti PSU dengan kapasitas daya yang lebih baik."
    },
    "Overheat (Prosesor)": {
        "gejala": ["suara_kipas_bising", "pc_mati_tiba_tiba", "casing_panas"],
        "solusi": "Bersihkan tumpukan debu pada heatsink (kipas prosesor) dan oleskan kembali thermal paste pada permukaan prosesor."
    },
    "VGA Bermasalah": {
        "gejala": ["garis_di_layar", "resolusi_kacau"],
        "solusi": "Cek kabel monitor. Update atau install ulang driver VGA. Jika menggunakan VGA card fisik, coba cabut dan bersihkan pinnya."
    },
    "Hardisk Corrupt": {
        "gejala": ["booting_lama", "suara_kasar_hdd", "pesan_disk_error"],
        "solusi": "Segera backup data penting Anda selagi bisa terbaca! Gunakan software seperti HDD Sentinel untuk mengecek 'Health' hardisk, dan pertimbangkan beralih ke SSD."
    }
}

daftar_pertanyaan = {
    "bunyi_beep": "Apakah terdengar bunyi beep panjang/berulang saat PC dinyalakan?",
    "layar_blank": "Apakah layar monitor tidak menampilkan apa-apa (blank hitam) padahal PC menyala?",
    "sering_restart": "Apakah PC sering merestart sendiri secara tiba-tiba?",
    "mati_saat_beban_berat": "Apakah PC mati saat digunakan untuk tugas berat (misal: main game/render)?",
    "suara_kipas_bising": "Apakah suara kipas di dalam casing terdengar sangat bising/keras?",
    "pc_mati_tiba_tiba": "Apakah PC mati seketika (tanpa proses shutdown Windows)?",
    "casing_panas": "Apakah area sekitar prosesor/casing terasa sangat panas saat disentuh?",
    "garis_di_layar": "Apakah muncul garis-garis aneh, kotak-kotak, atau warna kacau di monitor?",
    "resolusi_kacau": "Apakah resolusi layar tiba-tiba menjadi sangat besar dan tidak bisa diubah?",
    "booting_lama": "Apakah proses masuk ke Windows (booting) memakan waktu sangat lama?",
    "suara_kasar_hdd": "Apakah terdengar suara bunyi klik atau 'krek-krek' dari dalam casing PC?",
    "pesan_disk_error": "Apakah muncul pesan 'Disk Read Error' atau 'No Bootable Device' di layar hitam?"
}

def tanya_gejala():
    print("Jawablah pertanyaan berikut dengan 'y' untuk Ya atau 't' untuk Tidak.\n")

    for kode_gejala, teks_pertanyaan in daftar_pertanyaan.items():
        jawaban = input(f"{teks_pertanyaan} (y/t): ").strip().lower()
        if jawaban == 'y':
            gejala_pengguna.append(kode_gejala)

def jalankan_diagnosa():
    print("\n" + "="*40)
    print("HASIL ANALISIS SISTEM PAKAR".center(40))
    print("="*40)
    
    terdeteksi = False
    
    for nama_kerusakan, detail in basis_pengetahuan.items():
        gejala_penyakit = detail["gejala"]
        
        if all(g in gejala_pengguna for g in gejala_penyakit):
            print(f"TERDETEKSI MASALAH: {nama_kerusakan}")
            print(f"SOLUSI SINGKAT   : {detail['solusi']}\n")
            terdeteksi = True

    if not terdeteksi:
        print("STATUS: TIDAK TERDETEKSI")
        print("Pesan : Sistem tidak menemukan kerusakan spesifik berdasarkan gejala yang Anda masukkan.")
        print("Coba periksa kembali gejala yang dialami, atau bawa PC ke teknisi terdekat jika masalah berlanjut.")

def main():
    tanya_gejala()
    jalankan_diagnosa()

if __name__ == "__main__":
    main()