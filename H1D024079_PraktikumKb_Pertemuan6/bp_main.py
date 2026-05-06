import numpy as np
import backpropagation as b

# Inisialisasi input dan target (Bipolar XOR)
X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
t = np.array([[-1], [1], [1], [-1]])

# Pemanggilan model Backpropagation
# Parameter: alpha=0.3, epoch=30, target_error=0.001
model = b.Backpropagation(alpha=0.2, epoch=50, target_error=0.001)
model.fit(X, t)