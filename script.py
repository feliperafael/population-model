#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:16:12 2018

@author: Felipe Rafael de Souza
"""
import matplotlib.pyplot as plt
import pandas as pd

#source
#https://ourworldindata.org/world-population-growth
#https://ourworldindata.org/future-population-growth
k = 0.022 # population growth rate by year
initial_population = 2.556 # in billions - 1900
max_population = 10 # in billions http://www.bbc.com/earth/story/20160311-how-many-people-can-our-planet-really-support

def population_exponential(population_now, k):
    return population_now + k*population_now


def population_logistic(population_now, k):
    return population_now + k*population_now*(max_population - population_now)/max_population 


def plot(population_by_year, years):
    plt.plot(years, population_by_year)
    plt.ylabel("population of the earth in billions")
    plt.xlabel("year")
    
    plt.show()
    
time = 150 # in years
start_year = 1950
years = range(start_year, start_year+time, 1)

data_growth_rates = pd.read_csv('input/population-growth-rates.csv')
print(data_growth_rates['growth_rate'])
population_by_year = [initial_population]

for year in years:    
    k = (data_growth_rates['growth_rate'][year-start_year])/100.0
    population_by_year.append(population_exponential(population_by_year[year - start_year], k))

years.append(years[-1]+1) # add last year

plot(population_by_year,years)
print(str(start_year+time)+" population", str(population_by_year[-1])+" billions")
