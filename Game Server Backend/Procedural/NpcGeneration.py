# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 20:54:44 2018

@author: Tanasha
"""
import pandas as pd
import random
import numpy as np
possibilitiesArray = {'Race':[3], 'Gender': [2], 'GenderIdentity': [3], 'Personality':[16], 'Sexuality':[4], 'RightArm': [5], 'LeftArm': [5], 'RightLeg': [5], 'LeftLeg': [5], 'Head': [5], 'Torso': [7]}


'''for genes in possibilitiesArray.keys():
    limitedGenes.append([])'''
    
def InitiatePossibilities(genesDf):
    possibilityArray = []
    for i in genesDf.columns:
        possibilityArray.append(genesDf.xs(0)[i])
    return possibilityArray
        
def InitiateDataframe(col):
    return pd.DataFrame(columns = [0,1])

def GeneratePopulation(initialPopulation, populationDf, possibilityArray,limitedGenes = [],isLimited = False):
    totalPopulation = []
    for i in range(0,initialPopulation):
        appendArray = []
        for j in range(len(possibilityArray)):
            if isLimited == True:
                appendArray.append(random.choice(limitedGenes[j]))
            else:
                appendArray.append(random.randint(1,possibilityArray[j]))
        totalPopulation.append(appendArray)
    populationDataframe = pd.DataFrame(data = totalPopulation)
    return populationDataframe

def CreateNewPopulation(possibilitiesArray, populationCap, limitedGenes = [], isLimited = False):
    populationChoice = random.randrange(populationCap/2, populationCap)
    df = pd.DataFrame(data=possibilitiesArray)
    col = len(possibilitiesArray.keys())
    pArray = InitiatePossibilities(df)
    dF = InitiateDataframe(col)
    print(dF.columns)
    popDf = GeneratePopulation(populationChoice,dF,pArray,limitedGenes, isLimited)
    popDf.columns = df.columns
    return popDf
    
populationDF = CreateNewPopulation(possibilitiesArray, 1000000);