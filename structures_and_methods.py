# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:29:23 2019

@author: Matthew Wolf

Example Loan:
    1, 410000, 'Coffee', 'South America', 'Peru', 'Low', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Moderate Poverty', 'No', 'Yes', 315, 34, 0.00427, 37323, -19215, -8444, -5215, 4449

"""

class Loan(object):
    def __init__(self, loan_number, loan_amount, industry, lending_region, country, \
                 additionality, climate_change, bio_diversity, soil_degradation, \
                 water_scarcity, certification, sust_forestry, clean_tech, poverty_level, \
                 gender, livelihood, farmers_employees, female_farmers_employees, \
                 default_prob, exp_revenue, exp_op_costs, exp_cost_debt, \
                 exp_cost_risk, exp_net_income):
        self.loan_number = loan_number
        self.loan_amount = loan_amount
        self.industry = industry
        self.lending_region = lending_region
        self.country = country
        self.additionality = additionality
        self.climate_change = climate_change
        self.bio_diversity = bio_diversity
        self.soil_degradation = soil_degradation
        self.water_scarcity = water_scarcity
        self.certification = certification
        self.sust_forestry = sust_forestry
        self.clean_tech = clean_tech
        self.poverty_level = poverty_level
        self.gender = gender
        self.livelihood = livelihood
        self.farmers_employees = farmers_employees
        self.female_farmers_employees = female_farmers_employees
        self.default_prob = default_prob
        self.exp_revenue = exp_revenue
        self.exp_op_costs = exp_op_costs
        self.exp_cost_debt = exp_cost_debt
        self.exp_cost_risk = exp_cost_risk
        self.exp_net_income = exp_net_income
        
    def get_loan_number(self):
        return self.loan_number
    
    def get_loan_amount(self):
        return self.loan_amount
    
    def get_industry(self):
        return self.industry
    
    def get_lending_region(self):
        return self.lending_region
    
    def get_country(self):
        return self.country
    
    def get_additionality(self):
        return self.additionality
    
    def get_climate_change(self):
        return self.climate_change
    
    def get_bio_diversity(self):
        return self.bio_diversity
    
    def get_soil_degradation(self):
        return self.soil_degradation
    
    def get_water_scarcity(self):
        return self.water_scarcity
    
    def get_certification(self):
        return self.certification
    
    def get_sust_forestry(self):
        return self.sust_forestry
    
    def get_clean_tech(self):
        return self.clean_tech
    
    def get_poverty_level(self):
        return self.poverty_level
    
    def get_gender(self):
        return self.gender
    
    def get_livelihood(self):
        return self.livelihood
    
    def get_farmers_employees(self):
        return self.farmers_employees
    
    def get_female_farmers_employees(self):
        return self.female_farmers_employees
    
    def get_default_prob(self):
        return self.default_prob
    
    def get_exp_revenue(self):
        return self.exp_revenue
    
    def get_exp_op_costs(self):
        return self.exp_op_costs
    
    def get_cost_debt(self):
        return self.exp_cost_debt
    
    def get_cost_risk(self):
        return self.exp_cost_risk
    
    def get_exp_net_income(self):
        return self.exp_net_income
    
    def livelihoods_points(self):
        # max points contribution: 1.0
        if self.livelihood == 'Yes':
            return 1.0
        else:
            return 0.0
    
    def environment_and_climate_points(self):
        # max points contribution: 1.0
        rating = 0
        if self.certification == 'Yes':
            rating = rating + 0.5
        if self.sust_forestry == 'Yes':
            rating = rating + 0.25
        if self.clean_tech == 'Yes':
            rating = rating + 0.25
        return rating
    
    def scale_points(self):
        # max points contribution: 0.5
        rating = 0
        if self.farmers_employees >= 1500:
            rating = rating + 0.5
        if self.farmers_employees >= 500:
            rating = rating + 0.25
        return rating
    
    def poverty_level_points(self):
        # max points contribution: 0.5
        rating = 0    
        if self.poverty_level == 'Extreme Poverty':
            rating = rating + 0.5
        elif self.poverty_level == 'High Poverty':
            rating = rating + 0.25
        else:
            rating = rating
        return rating
        
    def environmental_vulnerability_points(self):
        # max points contribution: 0.5
        rating = 0
        if self.bio_diversity == "Yes":
            rating = rating + 1
        if self.soil_degradation == "Yes":
            rating = rating + 1
        if self.water_scarcity == "Yes":
            rating = rating + 1
        if self.climate_change == "Yes":
            rating = rating + 1

        if rating > 1:
            return 0.5
        elif rating > 0:
            return 0.25
        else: 
            return 0.0

    def additionality_points(self):
        if self.additionality == 'High':
            return 6.5
        elif self.additionality == 'Medium':
            return 3.0
        else:
            return 0.0    

    def get_impact_rating(self):
        rating = self.additionality_points() + \
                self.environmental_vulnerability_points() + \
                self.poverty_level_points() + \
                self.scale_points() + \
                self.environment_and_climate_points() + \
                self.livelihoods_points()        
        return rating
    
    def get_impact_group(self):
        if self.get_impact_rating() <= 3.0:
            return 'Low'
        elif self.get_impact_rating() <= 6.5:
            return 'Intermediate'
        else:
            return 'High'

test_loan = Loan(1, 410000, 'Coffee', 'South America', 'Peru', 'Low', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Moderate Poverty', 'No', 'Yes', 315, 34, 0.00427, 37323, -19215, -8444, -5215, 4449)

# 1. csv with columns in same order as arguments of __init__ of loan class
# 2. iterate through csv, adding each row to list of loans
# 3. Create Series of impact ratings, Series of expected incomes
# 4. Scatter of impact vs expected income

def plot_loans(loans):
    # intended to take DataFrame of loans data with needed columns to generate a 
    # scatter plot of Expected Impact (X) vs. Expected Net Income (Y) - either 
    # for a full universe or for a portfolio
    import pandas, seaborn
    df = pandas.DataFrame()
    for i in range(len(loans)):
        df.at[i, 'Loan Object'] = loans[i]
        df.at[i, 'Impact Rating'] = loans[i].get_impact_rating()
        df.at[i, 'Net Income'] = loans[i].get_exp_net_income()
        df.at[i, 'Impact Group'] = loans[i].get_impact_group()
    
    chart = seaborn.lmplot(x='Impact Rating',
           y='Net Income',
           data=df,
           hue='Impact Group',
           fit_reg=False)
    chart.set(ylim=(-40000,30000))
    chart.set(xlim=(0,10))

def greedy(loans, keyFunction):
    # Greedy algorithm, only constraint is we can only take 20 items
    # assumes loans is a list of loan instances, keyFunction is a class method
    # of the loan class
    
    loans_copy = sorted(loans, key=keyFunction, reverse=True)
    
    result = []
    
    total_expected_impact, total_expected_return = 0.0, 0.0
    
    for i in range(0,20):
        result.append(loans_copy[i])
        total_expected_impact += loans_copy[i].get_impact_rating()
        total_expected_return += loans_copy[i].get_exp_net_income()
    
    return result, total_expected_impact, total_expected_return

def test_greedy(loans, keyFunction):
    loaned, impact, net_income = greedy(loans, keyFunction)
    print('Total Impact Rating of Loans: ' + str(impact))
    print('Total Net Income of Loans:    $' + str(net_income))
    for loan in loaned:
        print('Loan #: ' + str(int(loan.get_loan_number())))
    plot_loans(loaned)

def test_greedies(loans):
    print('Use greedy by impact to choose loans in portfolio: ')
    test_greedy(loans, Loan.get_impact_rating)
    print('\nUse greedy by net income to choose loans in portfolio: ')
    test_greedy(loans, Loan.get_exp_net_income)
    print('\nUse greedy by # of female farmers or employees affected to choose loans in portfolio: ')
    test_greedy(loans, Loan.get_female_farmers_employees)

def randomPortfolios(loans, number):
    # assumes random has been imported already
    # loans is a list of loan instanes, number is an int for the number of random
    # portfolios desired
    import random
    portfolios = []
    for i in range(number):
        portfolio = random.sample(loans, 20)
        portfolios.append(portfolio)
    return portfolios
        
def calcPortfolioMetrics(portfolio):
    portfolio_impact = 0
    portfolio_income = 0
    for loan in portfolio:
        portfolio_impact += loan.get_impact_rating()
        portfolio_income += loan.get_exp_net_income()
    avg_impact = portfolio_impact / len(portfolio)
    if avg_impact <= 3.0:
        portfolio_impact_group = 'Low'
    elif avg_impact <= 6.5:
        portfolio_impact_group = 'Intermediate'
    else:
        portfolio_impact_group = 'High'
    avg_income = portfolio_income / len(portfolio)
    
    return portfolio_impact, portfolio_income, portfolio_impact_group, avg_income

def plotPortfolios(portfolios):
    # intended to take a list of loan instances (the portfolio) and generate a 
    # chart of their positions on the Efficient Impact Frontier
    import seaborn as sns
    sns.lmplot(x='impact',
           y='income',
           data=portfolios,
           hue='impact-group',
           fit_reg=False)
    



