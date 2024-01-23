import numpy as np
import random
from scipy.stats import norm
from scipy.stats import lognorm

import Community as Co


nB=475

# NSGA-II function
def nsga2(pop_size, num_generations):
    # Initialization
    population = []
    for _ in range(pop_size):
        Rft = random.randint(0, 5)  # Randomly initialize Rft
        i = random.randint(0, nB)  # Randomly initialize i
        reward, _, _, _, _, _, _, _ = Co.community(Rft, i)
        individual = {'Rft': Rft, 'i': i, 'reward': reward}
        population.append(individual)
    
    # Evolution
    for generation in range(num_generations):
        offspring = []
        for _ in range(pop_size):
            # Select parents using tournament selection
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            # Perform crossover and mutation
            child = crossover(parent1, parent2)
            child = mutate(child)
            
            # Evaluate the child's reward
            reward, _, _, _, _, _, _, _ = Co.community(child['Rft'], child['i'])
            child['reward'] = reward
            
            offspring.append(child)
        
        # Combine the parent and offspring populations
        population.extend(offspring)
        
        # Perform non-dominated sorting and crowding distance calculation
        population = fast_nondominated_sort(population)
        population = calculate_crowding_distance(population)
        
        # Select the next generation
        population = select_next_generation(population, pop_size)
    
    # Return the final population
    return population

def tournament_selection(population, tournament_size=2):
    selected = random.sample(population, tournament_size)
    selected.sort(key=lambda x: x['reward'], reverse=True)
    return selected[0]

def crossover(parent1, parent2, crossover_rate=0.9):
    child = {'Rft': parent1['Rft'], 'i': parent1['i'], 'reward': parent1['reward']}
    if random.random() < crossover_rate:
        child['Rft'] = parent2['Rft']
        child['i'] = parent2['i']
    return child

def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        individual['Rft'] = random.randint(0, 5)
        individual['i'] = random.randint(0, nB - 1)
    return individual

def fast_nondominated_sort(population):
    fronts = [[]]
    for individual in population:
        individual['dominated_count'] = 0
        individual['dominated_individuals'] = []
        for other_individual in population:
            if individual['reward'] < other_individual['reward']:
                individual['dominated_individuals'].append(other_individual)
            elif individual['reward'] > other_individual['reward']:
                individual['dominated_count'] += 1
        if individual['dominated_count'] == 0:
            fronts[0].append(individual)
    
    i = 0
    while len(fronts[i]) > 0:
        next_front = []
        for individual in fronts[i]:
            for dominated_individual in individual['dominated_individuals']:
                dominated_individual['dominated_count'] -= 1
                if dominated_individual['dominated_count'] == 0:
                    next_front.append(dominated_individual)
        i += 1
        fronts.append(next_front)
    
    return [individual for front in fronts[:-1] for individual in front]

def calculate_crowding_distance(population):
    for individual in population:
        individual['crowding_distance'] = 0.0
    
    num_objectives = 1  # Number of objectives (reward)
    
    for objective in range(num_objectives):
        population.sort(key=lambda x: x['reward'])
        population[0]['crowding_distance'] = float('inf')
        population[-1]['crowding_distance'] = float('inf')
        
        min_obj = population[0]['reward']
        max_obj = population[-1]['reward']
        
        if max_obj == min_obj:
            continue
        
        for i in range(1, len(population) - 1):
            population[i]['crowding_distance'] += (
                (population[i + 1]['reward'] - population[i - 1]['reward']) / (max_obj - min_obj)
            )
    
    return population

def select_next_generation(population, pop_size):
    population.sort(key=lambda x: x['crowding_distance'], reverse=True)
    next_generation = population[:pop_size]
    return next_generation

# Example usage
pop_size = 10
num_generations = 10
final_population = nsga2(pop_size, num_generations)

# Print the Pareto front (non-dominated solutions)
pareto_front = [individual for individual in final_population if individual['crowding_distance'] == float('inf')]
for individual in pareto_front:
    print('Rft:', individual['Rft'], 'i:', individual['i'], 'reward:', individual['reward'])