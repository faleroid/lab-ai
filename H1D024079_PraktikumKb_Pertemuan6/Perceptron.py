import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
  def __init__(self, alpha=0.1, epoch=10):
      self.alpha = alpha
      self.epoch = epoch

  def weighted_sum(self, X):
      return np.dot(X, self.w_[1:]) + self.w_[0]

  def predict(self, X):
      return np.where(self.weighted_sum(X) >= 0.0, 1, -1)

  def plot_decision_boundary(self, X, t, epoch):
      # Membuat titik data input
      plt.scatter(X[:, 0], X[:, 1], c=t.ravel(), marker='o',
      edgecolors='k', cmap=plt.cm.RdYlBu)
      # Menentukan limit tampilan bidang grafik
      x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
      y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
      # Membuat garis pemisah
      x_vals = np.linspace(x_min, x_max, 100)
      y_vals = -(self.w_[0] + self.w_[1] * x_vals) / self.w_[2]
      plt.plot(x_vals, y_vals, 'b-', label=f'Decision boundary (Epoch{epoch+1})')
      plt.xlim(x_min, x_max)
      plt.ylim(y_min, y_max)
      plt.title(f"Decision Boundary Pada Epoch {epoch+1}")
      plt.xlabel('X1')
      plt.ylabel('X2')
      plt.legend()
      plt.show()

  def fit(self, X, t):
      # Inisialisasi bobot dan bias awal = 0
      self.w_ = np.zeros(1 + X.shape[1])
      # Menyimpan hasil pada HasilPerceptron.txt
      with open("HasilPerceptron.txt", "w") as f:
          f.write("Masalah OR dengan Perceptron\n")
          f.write("----------------------------\n")
          f.write(f"Input :\n{X}\n")
          f.write(f"Target:\n{t}\n")
          f.write(f"Bobot awal : {self.w_[1:]}\n")
          f.write(f"Bias awal : {self.w_[0]}\n")
          f.write(f"Learning rate : {self.alpha}\n")
          f.write(f"Max Epoch : {self.epoch}\n")
          # Iterasi Perceptron(Epoch)
          for epoch in range(self.epoch):
              f.write(f"\nEpoch {epoch + 1}/{self.epoch}\n")
              f.write("----------\n")
              
              errors_in_epoch = [] # Collect errors for the current epoch
              # Iterasi setiap pasang matriks input dengan targetnya
              for xi, target in zip(X, t):
                  # Periksa input dengan model Perceptron
                  y_pred = self.predict(xi)
                  # Periksa apakah output sesuai target, jika iya maka
                  current_error = target - y_pred
                  errors_in_epoch.append(current_error)
                  
                  # Modifikasi bobot dengan Delta Rule
                  update = self.alpha * current_error
                  # Modifikasi bobot w
                  self.w_[1:] += update * xi
                  # Modifikasi bias b
                  self.w_[0] += update
                  # Menuliskan hasil tiap iterasi input pada satu epoch
                  f.write(f"Input: {xi}, Target: {target}, Predict: {y_pred}, Error: {current_error}, Bobot: {self.w_[1:]}, Bias: {self.w_[0]}\n")
              
              # After processing all inputs in the current epoch
              epoch_sse = sum(np.array(errors_in_epoch) ** 2)
              f.write(f"Sum Square Error(SSE): {epoch_sse}\n")
              
              # Simulasikan garis pemisah model Perceptron (plot once per epoch)
              self.plot_decision_boundary(X, t, epoch)
              
              # Periksa kondisi berhenti, jika penjumlahan kuadrat error setiap input = 0 atau max epoch tercapai
              if epoch_sse == 0:
                  f.write("--------------------------------------------------------------------------------\n")
                  f.write(f"Pelatihan berhenti pada epoch ke-{epoch + 1} karena ")
                  f.write("Sum Square Error(SSE) mencapai target.\n")
                  # Menuliskan bobot terakhir
                  f.write(f"\nBobot akhir :{self.w_[1:]}\n")
                  f.write(f"Bias akhir :{self.w_[0]}")
                  break
              elif epoch + 1 == self.epoch:
                  f.write("--------------------------------------------------------------------------------\n")
                  f.write(f"Pelatihan berhenti pada epoch ke-{epoch + 1} karena ")
                  f.write("max epoch tercapai.\n")
                  # Menuliskan bobot terakhir
                  f.write(f"\nBobot akhir :{self.w_[1:]}\n")
                  f.write(f"Bias akhir :{self.w_[0]}")
                  break