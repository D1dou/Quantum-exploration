# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 21:10:29 2023

@author: Dima DHEHIBI
"""

import numpy as np

def initialize(n):
    # Initialise un état superposé
    psi = np.ones(2**n) / np.sqrt(2**n)
    return psi

def oracle(n, target_state):
    # Crée une matrice oracle qui effectue une "inversion de phase"
    O = np.identity(2**n)
    O[target_state, target_state] = -1
    return O

def diffuser(n):
    # Crée une matrice de diffusion (inversion autour de la moyenne)
    psi_average = np.ones((2**n, 2**n)) / 2**n
    U = 2 * psi_average - np.identity(2**n)
    return U

def grover(n, target_state):
    # Effectue l'algorithme de Grover
    psi = initialize(n)
    O = oracle(n, target_state)
    U = diffuser(n)
    
    for _ in range(int(np.pi/4*np.sqrt(2**n))): # Approximativement √N itérations
        psi = np.dot(O, psi) # Applique l'oracle
        psi = np.dot(U, psi) # Applique la diffusion - ou la symétrie

    # Mesurer la probabilité
    probabilities = np.abs(psi)**2
    return probabilities

# Paramètres de simulation
n_qubits = 3 # Par exemple, pour une liste de 8 éléments (2^3)
target = 5 # Nous recherchons l'index 5 dans la liste

# Exécuter l'algorithme de Grover
probabilities = grover(n_qubits, target)

# Afficher les résultats
for i, p in enumerate(probabilities):
    print(f"Élément {i}: Probabilité = {p:.2f}")

# Trouver l'élément avec la plus haute probabilité
predicted_target = np.argmax(probabilities)
print(f"\nL'élément le plus probable est l'élément {predicted_target}, avec une probabilité de {probabilities[predicted_target]:.2f}")
