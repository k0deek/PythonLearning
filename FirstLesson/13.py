import numpy as np
from math import fabs as abs


A = np.array([[1, 0, 2], [2, -1, 1], [1, 3, -1]], dtype=int)
detA = np.linalg.det(A)
print('||A|| = ', detA)
detA2 = np.linalg.det(np.linalg.inv(A))
print(abs(detA * detA2 - 1) < 0.000001)
