import streamlit as st

rules_pakar = {
    ("Sangat Dingin", "Sepi"): "Sangat Nyaman",
    ("Sangat Dingin", "Sedang"): "Cukup Nyaman",
    ("Sangat Dingin", "Penuh Sesak"): "Tidak Nyaman",
    
    ("Normal", "Sepi"): "Sangat Nyaman",
    ("Normal", "Sedang"): "Cukup Nyaman",
    ("Normal", "Penuh Sesak"): "Tidak Nyaman",
    
    ("Panas", "Sepi"): "Cukup Nyaman",
    ("Panas", "Sedang"): "Tidak Nyaman",
    ("Panas", "Penuh Sesak"): "Sangat Tidak Nyaman"
}

def diagnosa_pakar(suhu, kepadatan):
    return rules_pakar.get((suhu, kepadatan), "Kondisi tidak terdefinisi dalam basis aturan")

st.set_page_config(page_title="Pakar Kenyamanan")
st.title("Sistem Pakar Kenyamanan Transportasi")

fakta_suhu = st.selectbox(
    "Pilih Fakta Kondisi Suhu Kabin:",
    ["Sangat Dingin", "Normal", "Panas"]
)

fakta_kepadatan = st.selectbox(
    "Pilih Fakta Kepadatan Penumpang:",
    ["Sepi", "Sedang", "Penuh Sesak"]
)

if st.button("Diagnosa Kenyamanan", type="primary"):
    keputusan = diagnosa_pakar(fakta_suhu, fakta_kepadatan)
    
    st.markdown("### Hasil Diagnosa Pakar:")
    if "Sangat Tidak Nyaman" in keputusan or "Tidak Nyaman" in keputusan:
        st.error(f"Kesimpulan: **{keputusan}**")
    elif "Cukup" in keputusan:
        st.warning(f"Kesimpulan: **{keputusan}**")
    else:
        st.success(f"Kesimpulan: **{keputusan}**")