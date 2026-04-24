import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def hitung_fuzzy(val_suhu, val_kepadatan):
    suhu = ctrl.Antecedent(np.arange(16, 41, 1), 'suhu')
    kepadatan = ctrl.Antecedent(np.arange(0, 101, 1), 'kepadatan')
    kenyamanan = ctrl.Consequent(np.arange(0, 101, 1), 'kenyamanan')

    suhu['dingin'] = fuzz.trapmf(suhu.universe, [16, 16, 22, 26])
    suhu['normal'] = fuzz.trimf(suhu.universe, [22, 26, 30])
    suhu['panas'] = fuzz.trapmf(suhu.universe, [26, 32, 40, 40])

    kepadatan['sepi'] = fuzz.trapmf(kepadatan.universe, [0, 0, 30, 50])
    kepadatan['sedang'] = fuzz.trimf(kepadatan.universe, [30, 50, 70])
    kepadatan['penuh'] = fuzz.trapmf(kepadatan.universe, [50, 75, 100, 100])

    kenyamanan['tidak_nyaman'] = fuzz.trimf(kenyamanan.universe, [0, 0, 50])
    kenyamanan['cukup_nyaman'] = fuzz.trimf(kenyamanan.universe, [25, 50, 75])
    kenyamanan['sangat_nyaman'] = fuzz.trimf(kenyamanan.universe, [50, 100, 100])

    rule1 = ctrl.Rule(suhu['panas'] | kepadatan['penuh'], kenyamanan['tidak_nyaman'])
    rule2 = ctrl.Rule(suhu['normal'] & kepadatan['sedang'], kenyamanan['cukup_nyaman'])
    rule3 = ctrl.Rule(suhu['dingin'] & kepadatan['sepi'], kenyamanan['sangat_nyaman'])
    rule4 = ctrl.Rule(suhu['dingin'] & kepadatan['sedang'], kenyamanan['cukup_nyaman'])
    rule5 = ctrl.Rule(suhu['normal'] & kepadatan['sepi'], kenyamanan['sangat_nyaman'])

    kenyamanan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    simulasi = ctrl.ControlSystemSimulation(kenyamanan_ctrl)
    
    simulasi.input['suhu'] = val_suhu
    simulasi.input['kepadatan'] = val_kepadatan
    simulasi.compute()
    
    return simulasi.output['kenyamanan']

st.set_page_config(page_title="Fuzzy Kenyamanan")
st.title("Pengukur Kenyamanan")

st.markdown("---")

suhu_input = st.slider("Suhu Kabin Saat Ini (°C)", 16.0, 40.0, 25.0, 0.5)
kepadatan_input = st.slider("Persentase Kepadatan Penumpang (%)", 0, 100, 50, 1)

if st.button("Hitung dengan Fuzzy", type="primary"):
    hasil = hitung_fuzzy(suhu_input, kepadatan_input)
    
    st.success(f"Skor: {hasil:.2f}%")
    st.progress(int(hasil))
    
    if hasil >= 70:
        st.info("Sangat Nyaman")
    elif hasil >= 40:
        st.warning("Cukup Nyaman")
    else:
        st.error("Tidak Nyaman")