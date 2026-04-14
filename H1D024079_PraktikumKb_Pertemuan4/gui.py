# Frame Tombol Jawaban (Disembunyikan di awal)
        self.frame_jawaban = tk.Frame(root)
        self.btn_ya = tk.Button(self.frame_jawaban, text="YA", width=10, command=lambda: self.jawab('y'))
        self.btn_tidak = tk.Button(self.frame_jawaban, text="TIDAK", width=10, command=lambda: self.jawab('t'))
        self.btn_ya.pack(side=tk.LEFT, padx=10)
        self.btn_tidak.pack(side=tk.LEFT, padx=10)

    def mulai_tanya(self):
        self.gejala_terpilih = []
        self.index_pertanyaan = 0
        self.btn_mulai.pack_forget() # Sembunyikan tombol mulai
        self.frame_jawaban.pack(pady=20)
        self.tampilkan_pertanyaan()

    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            self.label_tanya.config(text=teks)
        else:
            self.proses_hasil()

    def jawab(self, respon):
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)
            
        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    def proses_hasil(self):
        hasil = []
        for penyakit, syarat in database_penyakit.items():
            # Cek apakah gejala_terpilih mengandung semua syarat penyakit
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append(penyakit)
                
        kesimpulan = ", ".join(hasil) if hasil else "Tidak terdeteksi penyakit"
        messagebox.showinfo("Hasil Diagnosa", f"Berdasarkan gejala Anda:\n\n{kesimpulan}")
        
        # Reset ke awal
        self.frame_jawaban.pack_forget()
        self.btn_mulai.pack(pady=10)
        self.label_tanya.config(text="Diagnosa Selesai. Ingin mengulang?")

# Menjalankan Aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x250")
    app = AplikasiPakar(root)
    root.mainloop()