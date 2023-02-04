#
# CASH FLOW SIMULATOR
# Basic cash flow simulator that projects cash flow for a given number of weeks
# based on a set of scenarios and projects. Applicable to project based businesses.
#

# Import the necessary modules
import Project as p
import Scenarios as s

# Import packages
import datetime as dt
import random as rand
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define constants
VERSION = "0.1"

# Define variables
scenarios = []
projects = []
expense_items = []
weeks_to_simulate = 52
beginning_balance = 50000000
simulation_count = 1

# Define functions


def display_dollars(value):
    # Function to display a number as dollars
    return '${:,.2f}'.format(value)


def display_percentage(value):
    # Function to display a number as a percentage
    return '{:.2f}%'.format(value * 100)


# Greet the user and show the program version
print('─' * 25)
print("Cash Flow Simulator v" + VERSION)
print('─' * 25)
print()

# Create cash flow scenarios and display them
scenarios.append(s.Scenarios("Worst Case", 0.2))
scenarios.append(s.Scenarios("Expected Case", 0.5))
scenarios.append(s.Scenarios("Best Case", 0.8))

print('Loaded Scenarios:')
for s in scenarios:
    print(s.name + " - " + display_percentage(s.probability))
print()

# Show cash flow variables before simulation
print("Simulating " + str(weeks_to_simulate) + " weeks of cash flow")
print("Beginning balance: " + display_dollars(beginning_balance))
print("Simulation count: " + str(simulation_count))
print()

# Load input items from a file
# TODO: Load projects from Excel/CSV
print("Loaded " + str(len(projects)) + " projects")
# TODO: Load expense items from Excel/CSV
print("Loaded " + str(len(expense_items)) + " expense items")
print()

# Run the simulation
print("Running simulation...")
print()
for i in range(simulation_count):
    # Iterate through the number of simulations
    # TODO: Calculate cash flow for the simulation
    print("Simulation " + str(i + 1) + " of " +
          str(simulation_count) + "...")
    for scenario in scenarios:
        # Iterate through the scenarios for each simulation
        # TODO: Calculate cash flow for the scenario
        print("\tScenario: " + scenario.name)
        for week in range(0, weeks_to_simulate):
            # Iterate through the weeks for each scenario
            placeholder = 0  # temporary to allow code to run with loop
            # TODO: Calculate cash flow for the week
            # print("\t\tWeek " + str(week + 1) + " of " +
            #       str(weeks_to_simulate) + "...")
    print()
print("Simulation complete")
print()
