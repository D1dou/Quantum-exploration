# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Dima DHEHIBI
This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constantes
hbar = 1.0545718e-34  # Constante de Planck réduite
m = 9.10938356e-31    # Masse de l'électron
L = 1e-10             # Largeur du puits (en mètres)

def energy_levels(n):
    """ Calcule l'énergie du niveau n. """
    return n**2 * np.pi**2 * hbar**2 / (2 * m * L**2)

def psi(n, x):
    """ Calcule la fonction d'onde pour un niveau n donné et une position x. """
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def plot_wave_functions(num_levels):
    """ Affiche les fonctions d'onde pour les premiers 'num_levels' niveaux d'énergie. """
    x = np.linspace(0, L, 1000)
    for n in range(1, num_levels + 1):
        plt.plot(x, psi(n, x), label=f'n={n}')
    
    plt.legend()
    plt.xlabel('Position (m)')
    plt.ylabel('Fonction d’onde')
    plt.title('Fonctions d’onde pour une particule dans un puits de potentiel')
    plt.grid(True)
    plt.show()

def main():
    num_levels = 4  # Nombre de niveaux d'énergie à afficher
    plot_wave_functions(num_levels)
    for n in range(1, num_levels + 1):
        print(f"L'énergie du niveau {n} est: {energy_levels(n)} Joules")

if __name__ == '__main__':
    main()
