from ex5_functions import rand_matrix
from ex6_functions import *
import matplotlib.pyplot as plt

trials = [2,5,10,20,30,40,50,60]

# List of matrices to work with
matrices_A = []
matrices_B = []

# Creates random matrices.
for i,n in enumerate(trials):
    matrices_A.append(rand_matrix(n,n))
    matrices_B.append(rand_matrix(n,n))
        
my_times = []
native_times = []
    
for i in range(len(trials)): # Bad but what the heck, who cares
    my_times.append(take_time(matrices_A[i], matrices_B[i], False))
    native_times.append(take_time(matrices_A[i], matrices_B[i], True))

# Scatter plot.
plt.scatter(trials, my_times)
plt.scatter(trials, native_times)
plt.xlabel("Size")
plt.ylabel("Time")
plt.title("Time vs Size Matrix Multiplication")
plt.legend(["m_mult", "native"])
plt.show()

