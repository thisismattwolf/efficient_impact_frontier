# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:29:23 2019

@author: Matthew Wolf

Example Loan:
    1, 410000, 'Coffee', 'South America', 'Peru', 'Low', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Moderate Poverty', 'No', 'Yes', 315, 34, 0.00427, 37323, -19215, -8444, -5215, 4449

"""

class loan(object):
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
    
    def environement_and_climate_points(self):
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

    def get_additionality_points(self):
        if self.additionality == 'High':
            return 6.5
        elif self.additionality == 'Medium':
            return 3.0
        else:
            return 0.0    
        
    """
    def __str__(self):
        return ('#' + str(self.loan_number) \
        + '\n Loan Amount: $' + str(self.loan_amount) \
        + '\n Industry: ' + str(self.industry) + \
        + '\n Lending Region: ' + str(self.lending_region) \
        + '\n Country: ' + str(self.country) + \
        + '\n Loan Additionality: ' + str(self.additionality) \
        + '\n Climate Change Hotspot?: ' + str(self.climate_change) \
        + '\n Biodiversity Hotspot?: ' + str(self.bio_diversity) \
        + '\n Soil Degradation Hotspot?: ' + str(self.soil_degradation) \
        + '\n Water Scarcity Hotspot?: ' + str(self.water_scarcity) \
        + '\n Certification?: ' + str(self.certification) \
        + '\n Trees for conservation or carbon capture?: ' + str(self.sust_forestry) \
        + '\n Clean tech for emissions reduction?: ' + str(self.clean_tech) \
        + '\n Poverty Level: ' + str(self.poverty_level) \
        + '\n Gender Inclusion?: ' + str(self.gender) \
        + '\n Livelihood Improvement: ' + str(self.livelihood) \
        + '\n Farmers / Employees Impacted: ' + str(self.farmers_employees) \
        + '\n Female Farmers / Employees Impacted: ' + str(self.female_farmers_employees) \
        + '\n Probability of Default: ' + str(self.default_prob) \
        + '\n Expected Revenues: ' + str(self.exp_revenue) \
        + '\n Expected Operating Costs: ' + str(self.exp_op_costs) \
        + '\n Expected Cost of Debt: ' + str(self.exp_cost_debt) \
        + '\n Expected Cost of Risk: ' + str(self.exp_cost_risk) \
        + '\n Expected Net Loan Income: ' + str(self.exp_net_income))
        """

# Situation One
        
# 


# Constraints
"""
def netProfit(loans):
    for loan in loans:
        if loan.get_exp_net_income > 0:
            return True
        else:
            return False

def portfolio01Knapsack(items, constraintsFunction, valueFunction):
    # items is a list of all possible loans
    # constraints is a list of Boolean conditions to pass to filter()
    # value is a function
    itemsCopy = sorted(items, key=valueFunction, reverse=True)
    itemsFilter = filter(constraintsFunction, itemsCopy)
    return itemsFilter


# Try to upload the csv loan data into this data structure.
# Ranking of loans depends on sorted() with hyperargument 'key=keyFunction'.
        # Need to determine keyFunctions for 3 portfolios
# Is there something similar to sorted that acts as a filter, so we can set a
        # key function for constraints and then filter out loans based on that?
        # Could this all be done in Pandas without the data structure?
"""