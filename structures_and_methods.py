# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:29:23 2019

@author: Matthew Wolf
"""

class Loan(object):
    """========================================================================
    This class represents a Root Capital loan, including several attributes
    that represent the different financial and impact-related qualities of the
    loan.
    ========================================================================"""
    def __init__(self, loan_number, loan_amount, industry, lending_region, country, \
                 additionality, climate_change, bio_diversity, soil_degradation, \
                 water_scarcity, certification, sust_forestry, clean_tech, poverty_level, \
                 gender, livelihood, farmers_employees, female_farmers_employees, \
                 default_prob, exp_revenue, exp_op_costs, exp_cost_debt, \
                 exp_cost_risk, exp_net_income, \
                 impact_function):
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
        self.impact_function = impact_function
        
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
    
    def get_impact_rating(self):
        return self.impact_function
    
    def get_root_capital_impact_rating(self):
        points = 0
        # +1 point if livelihood == True
        if self.livelihood == True:
            points += 1.0
        
        # at most +1 for environmental /
        # sustainability traits
        if self.certification == True:
            points += 0.5
        if self.sust_forestry == True:
            points += 0.25
        if self.clean_tech == True:
            points += 0.25
        
        # at most +0.5 points for scale
        if self.farmers_employees >= 1500:
            points += 0.5
        elif self.farmers_employees >= 500:
            points += 0.25
        
        # at most +1 point for poverty level   
        if self.poverty_level == 'Extreme Poverty':
            points += 0.5
        elif self.poverty_level == 'High Poverty':
            points += 0.25
        
        # at most 0.5 points for environmental vulnerability
        temp = 0
        if self.bio_diversity == True:
            temp += 1
        if self.soil_degradation == True:
            temp += 1
        if self.water_scarcity == True:
            temp += 1
        if self.climate_change == True:
            temp += 1

        if temp > 1:
            points += 0.5
        elif temp > 0:
            points += 0.25
        
        #6.5 points if high, 3 if medium
        if self.additionality == 'High':
            points += 6.5
        elif self.additionality == 'Medium':
            points += 3.0
        
        return points
    
    def get_root_capital_impact_group(self):
        if self.get_root_capital_impact_rating() > 6.5:
            return 'High'
        elif self.get_root_capital_impact_rating() > 3.0:
            return 'Intermediate'
        else:
            return 'Low'

class Portfolio(object):
    """========================================================================
    This class represents a portfolio of Root Capital loans. It is a typical
    Python list of Loan class instances. Its methods calculate portfolio 
    metrics and characteristics. The method portfolio_stats() prints these 
    stats. 
    ========================================================================"""
    def __init__(self, loans): 
        self.loans = loans.copy()
        # Number of loans in portfolio
        self.n = len(self.loans)
        
    def add_loan(self, loan):
        if loan in self.loans:
            print("Loan already in portfolio - not added.")
        else:
            self.loans.append(loan)
    
    def remove_loan(self, loan):
        if loan in self.loans:
            self.loans.remove(loan)
        else:
            print("Loan not in portfolio - cannot be removed.")
    
    # Total amount of portfolio's loans    
    def get_total(self):
        total = 0 
        for loan in self.loans:
            total += loan.get_loan_amount()
        return total
    
    # List of unique IDs for loans
    def get_loan_numbers(self):
        numbers = []
        for loan in self.loans:
            numbers.append(loan.get_loan_number())
        return numbers
    
    # List of amounts for loans
    def get_loan_amounts(self):
        amounts = []
        for loan in self.loans:
            amounts.append(loan.get_loan_amount())
        return amounts
    
    # List of industries for loans
    def get_industries(self):
        industries = []
        for loan in self.loans:
            industries.append(loan.get_industry())
        return industries
    
    # List of lending regions for loans
    def get_regions(self):
        regions = []
        for loan in self.loans:
            regions.append(loan.get_lending_region())
        return regions
    
    # List of countries for loans
    def get_countries(self):
        countries = []
        for loan in self.loans:
            countries.append(loan.get_country())
        return countries
    
    # List of additionalities for loans
    def get_additionalities(self):
        additionalities = []
        for loan in self.loans:
            additionalities.append(loan.get_additionality())
        return additionalities
    
    # List of default probabilities for loans
    def get_default_probs(self):
        probs = []
        for loan in self.loans:
            probs.append(loan.get_default_prob())
        return probs
    
    # number of total farmers/employees supported through loans
    def get_farmers_employees(self):
        total = 0 
        for loan in self.loans:
            total += loan.get_farmers_employees()
        return total
    
    # number of total female farmers/employees supported through loans
    def get_female_farmers_employees(self):
        total = 0 
        for loan in self.loans:
            total += loan.get_female_farmers_employees()
        return total

    def get_total_net_income(self):
        total = 0
        for loan in self.loans:
            total += loan.get_exp_net_income()
        return total

    def get_total_revenue(self):
        total = 0
        for loan in self.loans:
            total += loan.get_exp_revenue()
        return total
    
    def get_total_impact_rating(self):
        total = 0
        for loan in self.loans:
            total += loan.get_impact_rating()
        return total
    
    def get_total_impact_group(self):
        rating = self.get_total_impact_rating()
        number = self.n
        if rating <= (number*3.0):
            return "Low"
        elif rating <= (number*6.5):
            return "Intermediate"
        else:
            return "High"
    
    def get_total_operating_expenses(self):
        total = 0
        for loan in self.loans:
            total += loan.get_exp_op_costs()
        return total
    
    def get_total_cost_debt(self):
        total = 0
        for loan in self.loans:
            total += loan.get_cost_debt()
        return total
    
    def get_total_cost_risk(self):
        total = 0
        for loan in self.loans:
            total += loan.get_cost_risk()
        return total
    
    def get_rate_of_return(self):
        return self.get_total_net_income() / self.get_total()
    
    def get_avg_default_risk(self):
        lists = self.get_loan_amounts(), self.get_default_probs()
        num = sum([x * y for x, y in zip(*lists)])
        return num / self.get_total()
    
    def portfolio_stats(self):
        print("=========================PORTFOLIO STATSTICS=========================")
        print("SCALE:")
        print("Total # of Loans:                           " + str(self.n))
        print("Total Loan Amount:                          " + str(self.get_total()))
        print("Total Farmers and Employees Reached:        " + str(self.get_farmers_employees()))
        print("Total Female Farmers and Employees Reached: " + str(self.get_female_farmers_employees()))
        print("=====================================================================")
        print("ADDITIONALITY:")
        print("% High Additionality:                       " + str(self.get_additionalities().count('High')/self.n))
        print("% Intermediate Additionality:               " + str(self.get_additionalities().count('Intermediate')/self.n))
        print("% Low Additionality:                        " + str(self.get_additionalities().count('Low')/self.n))
        print("=====================================================================")
        print("FINANCIAL PERFORMANCE:")
        print("Total Expected Net Income:                 $" + str(self.get_total_net_income()))
        print("Total Expected Revenue:                    $" + str(self.get_total_revenue()))
        print("Total Operating Expenses:                  $" + str(self.get_total_operating_expenses()))
        print("Total Cost of Debt:                        $" + str(self.get_total_cost_debt()))
        print("Total Cost of Risk:                        $" + str(self.get_total_cost_risk()))
        print("Weighted Average Default Risk:              " + str(self.get_avg_default_risk()))
        print("Portfolio Rate of Return:                   " + str(self.get_rate_of_return()))



"""===========================IMPACT VALUE FUNCTIONS===========================

This section contains functions that calculate the "impact" of Loan and 
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




