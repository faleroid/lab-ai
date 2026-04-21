rules_penyakit_tht = {
    "Tonsilitis": {"G37", "G12", "G5", "G27", "G6", "G21"},
    "Sinusitis Maksilaris": {"G37", "G12", "G27", "G17", "G33", "G36", "G29"},
    "Sinusitis Frontalis": {"G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"},
    "Sinusitis Edmoidalis": {"G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"},
    "Sinusitis Sfenoidalis": {"G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"},
    "Abses Peritonsiler": {"G37", "G12", "G6", "G15", "G2", "G29", "G10"},
    "Faringitis": {"G37", "G5", "G6", "G7", "G15"},
    "Kanker Laring": {"G5", "G27", "G6", "G15", "G2", "G19", "G1"},
    "Deviasi Septum": {"G37", "G17", "G20", "G8", "G18", "G25"},
    "Laringitis": {"G37", "G5", "G15", "G16", "G32"},
    "Kanker Leher & Kepala": {"G5", "G22", "G8", "G28", "G3", "G11"},
    "Otitis Media Akut": {"G37", "G20", "G35", "G31"},
    "Contact Ulcers": {"G5", "G2"},
    "Abses Parafaringeal": {"G5", "G16"},
    "Barotitis Media": {"G12", "G20"},
    "Kanker Nafasoring": {"G17", "G8"},
    "Kanker Tonsil": {"G6", "G29"},
    "Neuronitis Vestibularis": {"G35", "G24"},
    "Meniere": {"G20", "G35", "G14", "G4"},
    "Tumor Syaraf Pendengaran": {"G12", "G34", "G23"},
    "Kanker Leher Metastatik": {"G29"},
    "Osteosklerosis": {"G34", "G9"},
    "Vertigo Postular": {"G24"}
}

def diagnosa_tht(gejala_input):
    hasil_diagnosa = []
    
    for penyakit, gejala_syarat in rules_penyakit_tht.items():
        if gejala_syarat.issubset(gejala_input):
            hasil_diagnosa.append(penyakit)
            
    return hasil_diagnosa if hasil_diagnosa else ["Tidak terdeteksi penyakit"]

gejala_pasien_1 = {"G37", "G12", "G5", "G27", "G6", "G21"}
print(f"Gejala Pasien 1: {gejala_pasien_1}")
print(f"Hasil Diagnosa 1: {diagnosa_tht(gejala_pasien_1)}\n")

gejala_pasien_2 = {"G5", "G2", "G12", "G37"}
print(f"Gejala Pasien 2: {gejala_pasien_2}")
print(f"Hasil Diagnosa 2: {diagnosa_tht(gejala_pasien_2)}\n")

gejala_pasien_3 = {"G37", "G12", "G5", "G27", "G6"}
print(f"Gejala Pasien 3: {gejala_pasien_3}")
print(f"Hasil Diagnosa 3: {diagnosa_tht(gejala_pasien_3)}")