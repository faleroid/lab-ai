import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

kejelasan_informasi = ctrl.Antecedent(np.arange(0,101), 'kejelasan informasi')
kejelasan_prasyarat = ctrl.Antecedent(np.arange(0,101), 'kejelasan prasyarat')
kemampuan_petugas = ctrl.Antecedent(np.arange(0,101), 'kemampuan petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0,101), 'ketersediaan sarpras')
kepuasan_pelayanan = ctrl.Consequent(np.arange(0,401), 'kepuasan pelayanan')

kejelasan_informasi['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [0,0,50,75])
kejelasan_informasi['Cukup Memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [60,75,90])
kejelasan_informasi['Memuaskan'] = fuzz.trapmf(kejelasan_informasi.universe, [75,90,100,100])

kejelasan_prasyarat['Tidak Memuaskan'] = fuzz.trapmf(kejelasan_prasyarat.universe, [0,0,50,75])
kejelasan_prasyarat['Cukup Memuaskan'] = fuzz.trimf(kejelasan_prasyarat.universe, [60,75,90])
kejelasan_prasyarat['Memuaskan'] = fuzz.trapmf(kejelasan_prasyarat.universe, [75,90,100,100])

kemampuan_petugas['Tidak Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [0,0,50,75])
kemampuan_petugas['Cukup Memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [60,75,90])
kemampuan_petugas['Memuaskan'] = fuzz.trapmf(kemampuan_petugas.universe, [75,90,100,100])

ketersediaan_sarpras['Tidak Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [0,0,50,75])
ketersediaan_sarpras['Cukup Memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [60,75,90])
ketersediaan_sarpras['Memuaskan'] = fuzz.trapmf(ketersediaan_sarpras.universe, [75,90,100,100])

kepuasan_pelayanan['Tidak Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [0,0,50,75])
kepuasan_pelayanan['Kurang Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [50,75,100,150])
kepuasan_pelayanan['Cukup Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100,150,250,275])
kepuasan_pelayanan['Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250,275,325,350])
kepuasan_pelayanan['Sangat Memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [325,350,400,400])

# kejelasan_informasi.view()
# kejelasan_prasyarat.view()
# kemampuan_petugas.view()
# ketersediaan_sarpras.view()
# kepuasan_pelayanan.view()
# input("Tekan ENTER untuk melanjutkan")

# ==============================================================================
# 81 FUZZY RULES
# ==============================================================================

aturan1 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Kurang Memuaskan'])
aturan2 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan3 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan4 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan5 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan6 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan7 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan8 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan9 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

aturan10 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan11 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan12 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan13 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan14 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan15 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan16 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan17 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan18 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

aturan19 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan20 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan21 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan22 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan23 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan24 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan25 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan26 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan27 = ctrl.Rule(kejelasan_informasi['Tidak Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

aturan28 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan29 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan30 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan31 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan32 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan33 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan34 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan35 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan36 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])

aturan37 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan38 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan39 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan40 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan41 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan42 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan43 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan44 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan45 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

aturan46 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan47 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan48 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan49 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan50 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan51 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan52 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan53 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan54 = ctrl.Rule(kejelasan_informasi['Cukup Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

aturan55 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan56 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan57 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan58 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan59 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan60 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan61 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan62 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan63 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Tidak Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

aturan64 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Cukup Memuaskan'])
aturan65 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan66 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan67 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan68 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan69 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan70 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan71 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan72 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Cukup Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

aturan73 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan74 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan75 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Tidak Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan76 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Memuaskan'])
aturan77 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan78 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Cukup Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan79 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Tidak Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan80 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Cukup Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])
aturan81 = ctrl.Rule(kejelasan_informasi['Memuaskan'] & kejelasan_prasyarat['Memuaskan'] & kemampuan_petugas['Memuaskan'] & ketersediaan_sarpras['Memuaskan'], kepuasan_pelayanan['Sangat Memuaskan'])

engine = ctrl.ControlSystem([
    aturan1, aturan2, aturan3, aturan4, aturan5, aturan6, aturan7, aturan8, aturan9,
    aturan10, aturan11, aturan12, aturan13, aturan14, aturan15, aturan16, aturan17, aturan18,
    aturan19, aturan20, aturan21, aturan22, aturan23, aturan24, aturan25, aturan26, aturan27,
    aturan28, aturan29, aturan30, aturan31, aturan32, aturan33, aturan34, aturan35, aturan36,
    aturan37, aturan38, aturan39, aturan40, aturan41, aturan42, aturan43, aturan44, aturan45,
    aturan46, aturan47, aturan48, aturan49, aturan50, aturan51, aturan52, aturan53, aturan54,
    aturan55, aturan56, aturan57, aturan58, aturan59, aturan60, aturan61, aturan62, aturan63,
    aturan64, aturan65, aturan66, aturan67, aturan68, aturan69, aturan70, aturan71, aturan72,
    aturan73, aturan74, aturan75, aturan76, aturan77, aturan78, aturan79, aturan80, aturan81
])
system = ctrl.ControlSystemSimulation(engine)

system.input['kejelasan informasi'] = 80
system.input['kejelasan prasyarat'] = 60
system.input['kemampuan petugas'] = 50
system.input['ketersediaan sarpras'] = 90

system.compute()

print(system.output['kepuasan pelayanan'])
kepuasan_pelayanan.view(sim=system)

input("Tekan ENTER untuk melanjutkan")