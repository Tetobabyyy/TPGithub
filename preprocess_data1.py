# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 15:42:30 2025

@author: Theop
"""

from sklearn.model_selection import train_test_split

def preprocess_data(data, testSize):
    """Nettoie, met en forme les données et prépare les ensembles de train et 
    de test"""
    train, test = train_test_split(data, test_size = testSize)
    return train, test