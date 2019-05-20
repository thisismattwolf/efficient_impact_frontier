# -*- coding: utf-8 -*-
"""
Created on Mon May 20 19:51:57 2019

@author: Matthew Wolf
===========================IMPACT VALUE FUNCTIONS===========================

This file contains functions that calculate the "impact" of Loan and 
Portfolio class instances according to different heuristics. 

============================================================================"""

def root_capital(loan):
    """=====================================
    This function takes a Loan class instance as its argument, and calculates
    the Expected Impact Rating according to Root Capital's Methodology.
    
    The methodology is detailed in the report, "The Investor's Perspective: 
    Constructing a portfolio on the efficient impact-financial frontier within
    one asset class", written by Root Capital and the Impact Management Project.
    
    It assigns an impact rating scaled from 0 to 10 (less to more impact) based
    on the loan's attributes. 
    
    The function returns a float value indicating the expected impact rating.
    
    INPUT:   Loan class instance
    OUTPUT:  Float from 0 to 10
    ====================================="""
    points = 0
    # +1 point if livelihood == True
    if loan.livelihood == True:
        points += 1.0
    
    # at most +1 for environmental / sustainability traits
    if loan.certification == True:
        points += 0.5
    if loan.sust_forestry == True:
        points += 0.25
    if loan.clean_tech == True:
        points += 0.25
    
    # at most +0.5 points for scale
    if loan.farmers_employees >= 1500:
        points += 0.5
    elif loan.farmers_employees >= 500:
        points += 0.25
    
    # at most +1 point for poverty level   
    if loan.poverty_level == 'Extreme Poverty':
        points += 0.5
    elif loan.poverty_level == 'High Poverty':
        points += 0.25
    
    # at most 0.5 points for environmental vulnerability
    temp = 0
    if loan.bio_diversity == True:
        temp += 1
    if loan.soil_degradation == True:
        temp += 1
    if loan.water_scarcity == True:
        temp += 1
    if loan.climate_change == True:
        temp += 1

    if temp > 1:
        points += 0.5
    elif temp > 0:
        points += 0.25
    
    #6.5 points if high, 3 if medium
    if loan.additionality == 'High':
        points += 6.5
    elif loan.additionality == 'Medium':
        points += 3.0
    
    return points

def gender(loan):
    """=====================================
    Assigns value primarily based on loan's gender-related attributes. More gender
    inclusivity or female beneficiaries / employees, more value.
    
    INPUT:   Loan class instance
    OUTPUT:  Float from 0 to 10
    ====================================="""
    points = 0
    
    # gender inclusive?
    if loan.gender:
        points += 4.0
    
    # % of female beneficiaries / employees?
    if loan.female_farmers_employees / loan.farmers_employees > 0.60:
        points += 2.0
    elif loan.female_farmers_employees / loan.farmers_employees >= 0.50:
        points += 1.0
    
    # poverty level?
    if loan.poverty_level == 'Extreme Poverty':
        points += 2.0
    elif loan.poverty_level == 'High Poverty':
        points += 1.0
    
    # additionality?
    if loan.additionality == 'High':
        points += 1.0
    elif loan.additionality == 'Medium':
        points += 0.5
    
    # livelihoods?
    if loan.livelihood :
        points += 1.0
        
    return points
    
    
def sustainability(loan):
    """=====================================
    Assigns value primarily based on loan's sustainability-related attributes. More
    sustainability, more value.
    
    INPUT:   Loan class instance
    OUTPUT:  Float from 0 to 10
    ====================================="""
    points = 0.0
    
    # various sustainability attributes, max of 7 points
    temp = 0.0
    if loan.climate_change:
        temp += 2.0
    if loan.certification:
        temp += 2.0
    if loan.clean_tech:
        temp += 2.0
    if loan.bio_diversity:
        temp += 1.0
    if loan.soil_degradation:
        temp += 1.0
    if loan.water_scarcity:
        temp += 1.0
    if loan.sust_forestry:
        temp += 1.0
    
    if temp > 7.0:
        points += 7.0
    else:
        points += temp
    
    # poverty level?
    if loan.poverty_level == 'Extreme Poverty':
        points += 1.0
    elif loan.poverty_level == 'High Poverty':
        points += 0.5
    
    # additionality?
    if loan.additionality == 'High':
        points += 1.0
    elif loan.additionality == 'Medium':
        points += 0.5
    
    # livelihoods?
    if loan.livelihood :
        points += 1.0
        
    return points

def random(loan):
    
    from random import random
    return random.random() * 10

def pure_financial(loan):
    pass

