# Import library
import numpy as np
import matplotlib.pyplot as plt

# Buat kelas Backpropagation
class Backpropagation:
    # Simpan learning rate, epoch, dan target error dalam konstruktor
    # serta inisialisasi bobot dan bias awal random
    def __init__(self, alpha, epoch, target_error):
        self.alpha = alpha
        self.epoch = epoch
        self.target_error = target_error
        
        # Arsitektur Jaringan
        self.n_input = 2
        self.n_hidden = 2
        self.n_output = 1
        
        # Inisialisasi bobot dan bias secara random (0 sampai 1)
        self.w_hidden = np.random.rand(self.n_input, self.n_hidden)
        self.b_hidden = np.random.rand(1, self.n_hidden)
        self.w_output = np.random.rand(self.n_hidden, self.n_output)
        self.b_output = np.random.rand(1, self.n_output)

    # Fungsi menerapkan fungsi aktivasi sigmoid bipolar atau tanh
    def bi_sigmoid(self, x):
        return np.tanh(x)

    # Fungsi menerapkan turunan fungsi aktivasi sigmoid bipolar atau tanh
    def deriv_bi_sigmoid(self, x):
        # Asumsi x adalah output yang sudah melalui fungsi tanh
        return 1 - x**2

    # Fungsi membuat simulasi penurunan Sum Square Error (SSE) setiap epoch
    def plot_error(self, errors, epoch):
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, epoch + 1), errors, linestyle='-', color='b', label='Error')
        
        final_error = errors[-1]
        plt.annotate(f'Epoch {epoch}, Error: {final_error:.4f}', 
                     xy=(epoch, final_error), 
                     xytext=(epoch - (epoch * 0.2), final_error + 0.05),
                     arrowprops=dict(facecolor='black', arrowstyle="->"),
                     fontsize=10, color='red')
        
        plt.title('Perbaikan Error Setiap Epoch')
        plt.xlabel('Epoch')
        plt.ylabel('Sum Square Error (SSE)')
        plt.grid(True)
        plt.legend()
        plt.show()

    # Fungsi utama Backpropagation
    def fit(self, X, t):
        errors_per_epoch = []
        
        # Menyimpan hasil pada hasilBackpropagation.txt
        with open("hasilBackpropagation.txt", "w") as f:
            f.write("Masalah XOR dengan Backpropagation\n")
            f.write("----------------------------------\n")
            f.write(f"Input :\n{X}\n\n")
            f.write(f"Target :\n{t}\n\n")
            f.write(f"Bobot awal hidden layer :\n{self.w_hidden}\n\n")
            f.write(f"Bias awal hidden layer :\n{self.b_hidden}\n\n")
            f.write(f"Bobot awal output layer :\n{self.w_output}\n\n")
            f.write(f"Bias awal output layer :\n{self.b_output}\n\n")
            f.write(f"Learning rate: {self.alpha}\n")
            f.write(f"Max Epoch : {self.epoch}\n\n")

            # Iterasi Backpropagation (epoch)
            for epoch in range(self.epoch):
                f.write(f"----------------------------------\n")
                f.write(f"Epoch {epoch + 1}/{self.epoch}\n")
                f.write(f"----------------------------------\n")
                
                total_error = 0
                count = 1
                outputs_current_epoch = []

                # Iterasi setiap pasang matriks input dengan targetnya
                for xi, target in zip(X, t):
                    xi = xi.reshape(1, self.n_input) # Reshape untuk operasi matriks
                    
                    f.write(f"Data ke-{count}\n")
                    f.write("----\n")
                    
                    # --- Forward Propagation ---
                    # Operasikan input dengan hidden layer
                    h_in = np.dot(xi, self.w_hidden) + self.b_hidden
                    h = self.bi_sigmoid(h_in)
                    
                    # Operasikan hidden layer dengan output layer
                    y_in = np.dot(h, self.w_output) + self.b_output
                    y = self.bi_sigmoid(y_in)
                    
                    outputs_current_epoch.append(y[0][0])
                    
                    # --- Backward Propagation ---
                    # Hitung error output layer terhadap target
                    error = target - y
                    total_error += np.sum(error**2)
                    
                    # Hitung delta output layer (d_y)
                    d_y = error * self.deriv_bi_sigmoid(y)
                    
                    # Hitung error hidden layer (error_h)
                    error_h = np.dot(d_y, self.w_output.T)
                    
                    # Hitung delta hidden layer (d_h)
                    d_h = error_h * self.deriv_bi_sigmoid(h)
                    
                    # Perbaiki bobot dan bias output layer
                    self.w_output += np.dot(h.T, d_y) * self.alpha
                    self.b_output += d_y * self.alpha
                    
                    # Perbaiki bobot dan bias hidden layer
                    self.w_hidden += np.dot(xi.T, d_h) * self.alpha
                    self.b_hidden += d_h * self.alpha
                    
                    # Log data ke file
                    f.write(f"Aktivasi Output: {y}\n")
                    f.write(f"Error: {error}\n")
                    f.write(f"Delta Output (d_y): {d_y}\n")
                    f.write("----\n")
                    count += 1

                # Hitung SSE pada setiap epoch
                average_error = total_error / len(X)
                errors_per_epoch.append(average_error)
                
                f.write(f"Sum Square Error (SSE) epoch ke-{epoch + 1}: {average_error}\n\n")

                # Cek kondisi berhenti
                if average_error < self.target_error or epoch + 1 == self.epoch:
                    f.write("----------------------------------\n")
                    f.write(f"Pelatihan berhenti pada epoch ke-{epoch + 1} karena ")
                    if average_error < self.target_error:
                        f.write("Sum Square Error (SSE) mencapai target.\n")
                    else:
                        f.write("max epoch tercapai.\n")
                    
                    f.write(f"Bobot akhir hidden layer :\n{self.w_hidden}\n")
                    f.write(f"Bobot akhir output layer :\n{self.w_output}\n")
                    
                    self.plot_error(errors_per_epoch, epoch + 1)
                    break