import random
"""
Dice Rolling Simulation
This module simulates rolling a large number of dice and analyzes the frequency
distribution of each face (1-6).
The program:
1. Rolls a specified number of dice (6,000,000 by default)
2. Tracks the frequency of each face appearing
3. Calculates and displays the percentage distribution for each face
This simulation demonstrates the law of large numbers, where the frequency
of each face should approach approximately 16.67% (1/6) as the number of
rolls increases.
Output format:
- Face: The dice face number (1-6)
- Frequency: Number of times each face appeared
- Percentage: Percentage of total rolls for each face
"""

print("Rolar de Dados")
total_dados = 6000000
# Coleta de faces de um dado
print("Lançando ", total_dados, " dados...")
frequencia = [0]*6
for _ in range(total_dados):
    face = random.randint(1, 6)
    frequencia[face-1] = frequencia[face-1] + 1


# Exibe as frequencias
print("Face\tFrequência\tPercentual")
for i in range(1,7):
    percentual = (frequencia[i-1] / total_dados) * 100
    print(f"{i}\t{frequencia[i-1]}\t\t{percentual:.2f}%")
