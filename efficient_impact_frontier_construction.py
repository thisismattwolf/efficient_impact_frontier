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


def data_prepare():
    """=====================================
    This function loads and prepares the loans data to be used in the analysis.
    It creates a Pandas df from the existing CSV of loans data, and uses each
    row of data to create a Loan class instance (see the structure_and_methods.py
    file) of that loan, and stores these instances in another column in the df.    
    ====================================="""
    
    import pandas as pd
    
    # To ensure that the data is uploaded with the correct dtypes
    field_converters={'Loan Number':str, 'Loan Amount (USD)':int, 'Industry':str, 'Lending Region':str, 'Country':str,\
                      'Loan Additionality':str, 'Climate Change Hotspot':bool, 'Biodiversity Hotspot':bool,\
                      'Soil Degradation Hotspot':bool, 'Water Scarcity Hotspot':bool, 'Certification':bool,\
                      'Planting & maintaining trees for biodiversity conservation and carbon capture':bool,\
                      'Clean & appropriate tech for reduced emissions and resource efficiency':bool, 'Poverty Level':str,\
                      'Gender Inclusion':bool, 'Livelihood Improvement':bool, 'Farmers & Employees':int,\
                      'Female \nFarmers & Employees':int, 'Probability of Default':float, 'Expected Revenue':float,\
                      'Expected Operating Expenses':float, 'Expected Cost of Debt':float, 'Expected Cost of Risk':float,\
                      'Expected Net Loan Income':float}
    
    # Upload the data to a dataframe
    data = pd.read_csv('data.csv', converters=field_converters)
    
    # Import the Loan() class
    from structures_and_methods import Loan
    
    # Create a Loan() instance for each row, add the instances to another col
    # of the df
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
                                    data.at[i, 'Expected Net Loan Income'] ,\
                                    0)
    
    # Use the Loan() class method get_impact_rating() to calculate the impact 
    # rating and group for each loan, add as columns to the df
    for i in data.index:
        data.at[i, 'Expected Impact Rating'] = data.at[i, 'Loan Object'].get_root_capital_impact_rating()
        if data.at[i, 'Expected Impact Rating'] <= 3:
            data.at[i, 'Impact Group'] = 'Low'
        elif data.at[i, 'Expected Impact Rating'] <= 6.5:
            data.at[i, 'Impact Group'] = 'Intermediate'
        else:
            data.at[i, 'Impact Group'] = 'High'

    # return the prepared df
    return data

def plot_loans(loans):
    """========================================================================
    This function uses the seaborn lib to plot a set of Loan() class instances
    along two axes - net income, and impact rating.
    The input 'loans' should be a Pandas dataframe with Loan() class instances 
    for the loans to be plotted in a column named 'Loan Object'.
    ========================================================================"""
    import pandas, seaborn
    df = pandas.DataFrame()
    for i in range(len(loans)):
        df.at[i, 'Loan Object'] = loans.at[i, 'Loan Object']
        df.at[i, 'Expected Impact Rating'] = loans.at[i, 'Loan Object'].get_root_capital_impact_rating()
        df.at[i, 'Net Income'] = loans.at[i, 'Loan Object'].get_exp_net_income()
        df.at[i, 'Impact Group'] = loans.at[i, 'Loan Object'].get_root_capital_impact_group()
    print(df.head())
    chart = seaborn.lmplot(x='Expected Impact Rating',
           y='Net Income',
           data=df,
           hue='Impact Group',
           fit_reg=False)
    #chart.set(ylim=(minIncome,maxIncome))
    #chart.set(xlim=(minImpact,maxImpact))

def randomPortfolios(loans, r, n):
    """========================================================================
    This function takes a list of Loan() objects in a Pandas dataframe, as well
    as two number: the desired number of random portfolios (r), and the number of 
    loans per portfolio (n). It then builds r Portfolio() instances of n Loan
    instances, and returns them in a Pandas dataframe with the column header, 
    "Portfolio Object".
    ========================================================================"""
    import random
    import pandas as pd
    from structures_and_methods import Portfolio
    portfolios = []
    for i in range(r):
        portfolio = Portfolio(random.sample(loans, n))
        portfolios.append(portfolio)
    portfolios = pd.DataFrame(portfolios, columns=["Portfolio Object"])
    return portfolios

def plot_portfolios(portfolios):

    """========================================================================
    This function uses the seaborn lib to plot a set of Portfolio() class
    instances along two axes - net income and impact rating.
    The input 'portoflios' should be a Pandas dataframe with Portfolio() class 
    instances for the loans to be plotted in a column named 'Portfolio Object'.
    ========================================================================"""
    import pandas, seaborn
    
    df = pandas.DataFrame()
    for i in range(len(portfolios)):
        df.at[i, 'Portfolio Object'] = portfolios.at[i, 'Portfolio Object']
        df.at[i, 'Required Subsidy'] = portfolios.at[i, 'Portfolio Object'].get_total_net_income()
        df.at[i, 'Impact Rating'] = portfolios.at[i, 'Portfolio Object'].get_total_impact_rating()
        df.at[i, 'Impact Group'] = portfolios.at[i, 'Portfolio Object'].get_total_impact_group()
        
    chart = seaborn.lmplot(x='Impact Rating', y='Required Subsidy', data=df,\
                           hue='Impact Group', fit_reg=False)
      
#TODO
        # 1. Allow Loan() class to take user-specified impact heuristic
        # 2. Allow Portfolio class to take user-specified impact heuristic
        # 3. Random portfolio generator with constraints
        # 4. portfolio_impact rebalance