# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 15:43:02 2025

@author: Theop
"""

def train_model(train_X, train_y, test_X, model):
    """entraine un modele ML de classification et retourne des predictions sur
    le dataset de test"""
    model.fit(train_X,train_y) 
    prediction=model.predict(test_X)
    return prediction
