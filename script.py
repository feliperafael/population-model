#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 20:16:12 2018

@author: Felipe Rafael de Souza
"""
import matplotlib.pyplot as plt

k = 0.022 # population growth rate by year
initial_population = 1.650 # in billions - 1900
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
start_year = 1900
years = range(start_year, start_year+time, 1)


population_by_year = [initial_population]

for year in years:
    population_by_year.append(population_logistic(population_by_year[year - start_year], k))
    
years.append(years[-1]+1) # add last year


plot(population_by_year,years)