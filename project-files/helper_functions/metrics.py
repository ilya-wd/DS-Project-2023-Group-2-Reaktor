import pandas as pd
import numpy as np

def calculate_species_richness (row):
    return np.sum(row.to_numpy() > 0.0)

def calculate_shannon_entropy (row):
    probabilities = row.to_numpy()
    probabilities = probabilities[np.where(probabilities > 0)]
    return -np.sum(probabilities*np.log2(probabilities))

def calculate_simpson_index (row):
    probabilities = row.to_numpy()
    return np.sum(probabilities * probabilities)

def generate_richness_frame (df):
    richness = df.apply(calculate_species_richness, axis = 1)
    richness = richness.to_frame()
    richness.columns = ['richness']
    richness.reset_index(inplace = True)
    return richness

def generate_shannon_frame (df):
    shannon_entropies = df.apply(calculate_shannon_entropy, axis = 1)
    shannon_entropies = shannon_entropies.to_frame()
    shannon_entropies.columns = ['shannon_entropy']
    shannon_entropies.reset_index(inplace = True)
    return shannon_entropies

def generate_simpson_frame (df):
    simpson_indices = df.apply(calculate_simpson_index, axis = 1)
    simpson_indices = simpson_indices.to_frame()
    simpson_indices.columns = ['simpson_index']
    simpson_indices.reset_index(inplace = True)
    return simpson_indices