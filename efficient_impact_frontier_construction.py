# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:40:41 2019

@author: Matthew Wolf

Based on Medium article by Bernard Brenyah at:
    https://medium.com/python-data/efficient-frontier-portfolio-optimization-with-python-part-2-2-2fe23413ad94
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

field_converters={'Loan Number':str, 'Loan Amount (USD)':int, 'Industry':str, 'Lending Region':str, 'Country':str,\
                  'Loan Additionality':str, 'Climate Change Hotspot':bool, 'Biodiversity Hotspot':bool,\
                  'Soil Degradation Hotspot':bool, 'Water Scarcity Hotspot':bool, 'Certification':bool,\
                  'Planting & maintaining trees for biodiversity conservation and carbon capture':bool,\
                  'Clean & appropriate tech for reduced emissions and resource efficiency':bool, 'Poverty Level':str,\
                  'Gender Inclusion':bool, 'Livelihood Improvement':bool, 'Farmers & Employees':int,\
                  'Female \nFarmers & Employees':int, 'Probability of Default':float, 'Expected Revenue':float,\
                  'Expected Operating Expenses':float, 'Expected Cost of Debt':float, 'Expected Cost of Risk':float,\
                  'Expected Net Loan Income':float}

data = pd.read_csv('data.csv', converters=field_converters)

from structures_and_methods import Loan

# Create Loan() class instances for each loan in the data
# Store these data instances in another column in the df
for i in data.index:
    
    data.at[i, 'Loan Object'] = Loan(data.at[i, 'Loan Number'] ,\
                                data.at[i, 'Loan Amount (USD)'] ,\
                                data.at[i, 'Industry'] ,\
                                data.at[i, 'Lending Region'] ,\
                                data.at[i, 'Country'] ,\
                                data.at[i, 'Loan Additionality'] ,\
                                data.at[i, 'Climate Change Hotspot'] ,\
                                data.at[i, 'Biodiversity Hotspot'] ,\
                                data.at[i, 'Soil Degradation Hotspot'] ,\
                                data.at[i, 'Water Scarcity Hotspot'] ,\
                                data.at[i, 'Certification'] ,\
                                data.at[i, 'Planting & maintaining trees for biodiversity conservation and carbon capture'],\
                                data.at[i, 'Clean & appropriate tech for reduced emissions and resource efficiency'] ,\
                                data.at[i, 'Poverty Level'] ,\
                                data.at[i, 'Gender Inclusion'] ,\
                                data.at[i, 'Livelihood Improvement'] ,\
                                data.at[i, 'Farmers & Employees'] ,\
                                data.at[i, 'Female Farmers & Employees'] ,\
                                data.at[i, 'Probability of Default'] ,\
                                data.at[i, 'Expected Revenue'] ,\
                                data.at[i, 'Expected Operating Expenses'] ,\
                                data.at[i, 'Expected Cost of Debt'] ,\
                                data.at[i, 'Expected Cost of Risk'] ,\
                                data.at[i, 'Expected Net Loan Income'])

# add the impact rating and impact group to the df
for i in data.index:
    
    data.at[i, 'Expected Impact Rating'] = data.at[i, 'Loan Object'].get_impact_rating()
    if data.at[i, 'Expected Impact Rating'] <= 3:
        data.at[i, 'Impact Group'] = 'Low'
    elif data.at[i, 'Expected Impact Rating'] <= 6.5:
        data.at[i, 'Impact Group'] = 'Intermediate'
    else:
        data.at[i, 'Impact Group'] = 'High'

# plot the individual loans in income vs impact terms
plt.style.use('seaborn-dark')
data.plot.scatter(x='Expected Impact Rating', y='Expected Net Loan Income',\
                  edgecolors='black',grid=True)

from structures_and_methods import randomPortfolios, calcPortfolioMetrics
