import matplotlib.pyplot as plt 

# core counts. 
cores = [2, 4, 8, 16] 

# execution times for each molecule with increasing number of cores. 
ANTCEN = [294.3, 283.8, 242.2, 196.3] 
PENCEN = [681.4, 666.7, 553.9, 466.6] 
TETCEN = [381.2, 373.4, 311.2, 255.7] 

# plotting each molecule on one graph. 
plt.plot(cores, ANTCEN, label='ANTCEN') 
plt.plot(cores, PENCEN, label='PENCEN') 
plt.plot(cores, TETCEN, label='TETCEN') 
plt.xlabel("Number of CPU cores", fontsize=12, weight='bold') 
plt.ylabel("Execution time (seconds)", fontsize=12, weight='bold') 
plt.title("Execution Time vs Core Count", fontsize=16, weight='bold') 
plt.legend() 
plt.grid() 
plt.show()
