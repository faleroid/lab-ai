import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

suhu = ctrl.Antecedent(np.arange(0,41), 'suhu')
kelembaban = ctrl.Antecedent(np.arange(0,101), 'kelembaban')
kecepatan = ctrl.Consequent(np.arange(0,101), 'kecepatan')

# suhu
suhu['Dingin'] = fuzz.zmf(suhu.universe, 0, 18)
suhu['Normal'] = fuzz.pimf(suhu.universe, 15, 25, 25, 35)
suhu['Panas'] = fuzz.smf(suhu.universe, 32, 40)

# kelembaban
kelembaban['Rendah'] = fuzz.trapmf(kelembaban.universe, [0,0,30,50])
kelembaban['Biasa'] = fuzz.trimf(kelembaban.universe, [30,50,70])
kelembaban['Tinggi'] = fuzz.trapmf(kelembaban.universe, [50,70,100,100])

# kecepatan
kecepatan['Rendah'] = fuzz.trapmf(kecepatan.universe, [0,0,10,50])
kecepatan['Normal'] = fuzz.trimf(kecepatan.universe, [30,50,70])
kecepatan['Tinggi'] = fuzz.trapmf(kecepatan.universe, [50,90,100,100])

suhu.view()
kelembaban.view()
kecepatan.view()
input("Tekan ENTER untuk melanjutkan")

aturan1 = ctrl.Rule(suhu['Dingin'], kecepatan['Rendah'])
aturan2 = ctrl.Rule(suhu['Normal'] & kelembaban['Biasa'], kecepatan['Normal'])
aturan3 = ctrl.Rule(suhu['Panas'], kecepatan['Tinggi'])
aturan4 = ctrl.Rule(suhu['Normal'] & kelembaban['Tinggi'], kecepatan['Tinggi'])
aturan5 = ctrl.Rule(suhu['Normal'] & kelembaban['Rendah'], kecepatan['Rendah'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3, aturan4, aturan5])
system = ctrl.ControlSystemSimulation(engine)

system.input['suhu'] = 10
system.input['kelembaban'] = 30
system.compute()
print(system.output['kecepatan'])
kecepatan.view(sim=system)
input("Tekan ENTER untuk melanjutkan")