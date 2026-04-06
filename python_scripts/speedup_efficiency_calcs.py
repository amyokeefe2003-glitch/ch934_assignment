# execution time for each molecule (ANTCEN, PENCEN, TETCEN, respectively) for the 2 core calculations. 
t_A_2core = 294.3 
t_P_2core = 681.4 
t_T_2core = 381.2 

# execution time for each molecule (ANTCEN, PENCEN, TETCEN, respectively) for the 4 core calculations. 
t_A_4core = 283.8 
t_P_4core = 666.7 
t_T_4core = 373.4 

# execution time for each molecule (ANTCEN, PENCEN, TETCEN, respectively) for the 8 core calculations. 
t_A_8core = 242.2 
t_P_8core = 553.9 
t_T_8core = 311.2 

# execution time for each molecule (ANTCEN, PENCEN, TETCEN, respectively) for the 16 core calculations. 
t_A_16core = 196.3 
t_P_16core = 466.6 
t_T_16core = 255.7 


# computing speedup for 4 core, 8 core, and 16 core calculations relative to the 2-core configuration, respectively, for ANTCEN. 
speedup_A_2_4 = t_A_2core / t_A_4core 
speedup_A_2_8 = t_A_2core / t_A_8core 
speedup_A_2_16 = t_A_2core / t_A_16core 

# printing above results. 
print("Speedups for 4 core, 8 core, and 16 core calculations, respectively, relative to the 2-core configuration for ANTCEN:") 
print(f"{speedup_A_2_4:.2f}") 
print(f"{speedup_A_2_8:.2f}") 
print(f"{speedup_A_2_16:.2f}") 

# computing speedup for 4 core, 8 core, and 16 core calculations relative to the 2-core configuration, respectively, for PENCEN. 
speedup_P_2_4 = t_P_2core / t_P_4core 
speedup_P_2_8 = t_P_2core / t_P_8core 
speedup_P_2_16 = t_P_2core / t_P_16core 

# printing above results. 
print("\nSpeedups for 4 core, 8 core, and 16 core calculations, respectively, relative to the 2-core configuration for PENCEN:") 
print(f"{speedup_P_2_4:.2f}") 
print(f"{speedup_P_2_8:.2f}") 
print(f"{speedup_P_2_16:.2f}") 

# computing speedup for 4 core, 8 core, and 16 core calculations relative to the 2-core configuration, respectively, for TETCEN. 
speedup_T_2_4 = t_T_2core / t_T_4core 
speedup_T_2_8 = t_T_2core / t_T_8core 
speedup_T_2_16 = t_T_2core / t_T_16core 

# printing above results. 
print("\nSpeedups for 4 core, 8 core, and 16 core calculations, respectively, relative to the 2-core configuration for TETCEN:") 
print(f"{speedup_T_2_4:.2f}") 
print(f"{speedup_T_2_8:.2f}") 
print(f"{speedup_T_2_16:.2f}") 


# computing efficiency for 4 core, 8 core, and 16 core calculations for ANTCEN. 
efficiency_A_4 = speedup_A_2_4 / 4 
efficiency_A_8 = speedup_A_2_8 / 8 
efficiency_A_16 = speedup_A_2_16 / 16 

# printing above results. 
print("\n\nEfficiencies for 4 core, 8 core, and 16 core calculations for ANTCEN:") 
print(f"{efficiency_A_4:.2f}") 
print(f"{efficiency_A_8:.2f}") 
print(f"{efficiency_A_16:.2f}") 

# computing efficiency for 4 core, 8 core, and 16 core calculations for PENCEN. 
efficiency_P_4 = speedup_P_2_4 / 4 
efficiency_P_8 = speedup_P_2_8 / 8 
efficiency_P_16 = speedup_P_2_16 / 16 

# printing above results. 
print("\nEfficiencies for 4 core, 8 core, and 16 core calculations for PENCEN:") 
print(f"{efficiency_P_4:.2f}") 
print(f"{efficiency_P_8:.2f}") 
print(f"{efficiency_P_16:.2f}") 

# computing efficiency for 4 core, 8 core, and 16 core calculations for TETCEN. 
efficiency_T_4 = speedup_T_2_4 / 4 
efficiency_T_8 = speedup_T_2_8 / 8 
efficiency_T_16 = speedup_T_2_16 / 16 

# printing above results. 
print("\nEfficiencies for 4 core, 8 core, and 16 core calculations for TETCEN:") 
print(f"{efficiency_T_4:.2f}") 
print(f"{efficiency_T_8:.2f}") 
print(f"{efficiency_T_16:.2f}")
