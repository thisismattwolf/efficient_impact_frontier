# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:29:23 2019

@author: Matthew Wolf


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



# Try to upload the csv loan data into this data structure.
 