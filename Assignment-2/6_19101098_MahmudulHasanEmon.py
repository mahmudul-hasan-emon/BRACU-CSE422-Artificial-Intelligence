#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import random
def fitness(population, n):
    clash=np.zeros(len(population))
    for q,chromosome in enumerate(population):
        cr = chromosome.tolist()
        row_col_clash= sum([cr.count(col)-1 for col in cr])/2
        clash[q]+=row_col_clash
        cl=0
        for i in range(len(chromosome)):
            for j in range(len(chromosome)):
                if ( i != j):
                    dx = abs(i-j)
                    dy = abs(chromosome[i] - chromosome[j])
                    if dx == dy:
                        cl+=1
        clash[q]+=(cl//2)         
    return  28-clash

def select(population, fit):
    fitness_values=fitness(population,n)
    probability=fitness_values/sum(fitness_values)
    selected_fitness=np.random.choice(fitness_values,1,True,p=probability)
    parent_index=fitness_values.tolist().index(selected_fitness[0])
    return population[parent_index]

def crossover(x, y):
    n = len(x)
    child = []    
    for i in range(n):
        child.append(-1)       
    cross_over_point = random.randint(1, n - 1)
    for i in range(cross_over_point):
        child[i] = x[i]        
    for i in range(cross_over_point, n):
        child[i]=y[i]        
    return child


def mutate(child):
    index_to_mutate = random.randint(0,7)
    gene_to_place = random.randint(1,8)
    child[index_to_mutate]=gene_to_place
    return child

def GA(population, n, mutation_threshold = 0.3):
    generation_fitness=[]
    generations = 0
    while 28 not in fitness(population,n) :
        new_population = []
        for i in range(len(population)):
            x=select(population,fitness)
            y=select(population,fitness)
            #select funtion
            child = crossover(x,y)
            if random.uniform(0.0,0.5) < mutation_threshold:
                child = mutate(child)
                new_population.append(child)      
    population = np.array(new_population)  
    population_fitness = fitness(population,n)
    generation_fitness.append(np.max(population_fitness))
    generation_fitness.append(np.min(population_fitness))
    generation_fitness.append(np.mean(population_fitness))
    generations+=1   
    best_fitness = np.max(fitness(population))  
    generation_fitness.append(best_fitness)
    index =  fitness(population).tolist().index(best_fitness)
    individual= population[index]
  
    print(f'selected individual --> {individual} \n')
    print(f'fitness --> {best_fitness} \n')
    print(f'Generations --> {generations} \n')
    print(f'{generation_fitness} \n')
    return



# In[ ]:




