author = 'rfontenay'
description = 'Genetic algorithm to solve a scheduling problem of N jobs on M parallel machines'
import random
import time
# ******************* JOHNSON’S RULE******************* #
a=[87,51,11,78,72,69,94,72] b=[98,45,28,88,64,49,64,59] comp01=[]
comp02=[]
left=[]
right=[]
for i in range(0,5):
t=min(a[i],b[i]) if(a[i]==t):
comp01=[t]+comp01 left=comp01 left.sort()
else:
comp02=[t]+comp02 right=comp02 right.sort(reverse=True)
left=left+right
print(left)
# ******************* Parameters ******************* # # Jobs processing times
jobsProcessingTime = left
# Number of jobs
n = len(jobsProcessingTime)
               # Number of machines
m= 2
# Genetic Algorithm : Population size GA_POPSIZE = 310
# Genetic Algorithm : Elite rate GA_ELITRATE = 0.1
# Genetic Algorithm : Mutation rate GA_MUTATIONRATE = 0.25
# Genetic Algorithm : Iterations number GA_ITERATIONS = 1000
# ******************* Functions ******************* #
def random_chromosome(): """
Description :Generate a chromosome with a random genome (for each job, assign a random machine).
Input : -Line 2 of comment...
Output : Random chromosome.
"""
# Jobs assignment : Boolean matrix with 1 line by job, 1 column by machine new_chromosome = [[0 for i in range(m)] for j in range(n)]
# For each job, assign a random machine for i in range(n):
new_chromosome[i][random.randint(0, m - 1)] = 1 return new_chromosome
def fitness(chromosome): """
Description : Calculate the score of the specified chromosome.
The score is the longest processing time among all the machines processing times. Input : A chromosome.
     
               Output : The score/fitness. """
max_processing_time = -1 for i in range(m):
machine_processing_time = 0 for j in range(n):
machine_processing_time += chromosome[j][i] * jobsProcessingTime[j] # Save the maximum processing time found
if machine_processing_time > max_processing_time:
max_processing_time = machine_processing_time return max_processing_time
def crossover(chromosome1, chromosome2): """
Description : Crossover two chromosomes by alternative genes picking. Input : Two chromosome.
Output : One chromosome.
"""
new_chromosome = [[0 for i in range(m)] for j in range(n)] for i in range(n):
# Alternate the pickup between the two selected solutions if not i % 2:
new_chromosome[i] = chromosome1[i] else:
new_chromosome[i] = chromosome2[i] return new_chromosome
def evolve(population): """
Description : Create a new population based on the previous population.
The new population is generated by mixing the best chromosomes of the previous population.
Input : Old population.
     
               Output : New population."""
new_population = [[] for i in range(GA_POPSIZE)] # First : Keep elites untouched
elites_size = int(GA_POPSIZE * GA_ELITRATE) for i in range(elites_size): # Elitism
new_population[i] = population[i]
# Then generate the new population
for i in range(elites_size, GA_POPSIZE):
# Generate new chromosome by crossing over two from the previous population new_population[i] = crossover(population[random.randint(0, GA_POPSIZE / 2)],
population[random.randint(0, GA_POPSIZE / 2)])
# Mutate
if random.random() < GA_MUTATIONRATE:
random_job = random.randint(0, n - 1)
# Reset assignment
new_population[i][random_job] = [0 for j in range(m)]
# Random re-assignment new_population[i][random_job][random.randint(0, m - 1)] = 1
return new_population
# ******************* Program ******************* #
# Measure execution time start = time.time()
# Generate an initial random population population = [[] for i in range(GA_POPSIZE)] for i in range(GA_POPSIZE):
population[i] = random_chromosome()
# Sort the population based on the fitness of chromosomes population = sorted(population, key=lambda c: fitness(c)) # Print initial best makespan
#print("makespan = %03d" % (fitness(population[0]))) #Iterate
     
for i in range(GA_ITERATIONS):
# Sort the population : order by chromosone's scores. population = sorted(population, key=lambda c: fitness(c)) #Generate the following generation (new population) population = evolve(population)
# Print the best fitness and the execution time after iterations print("Ending makespan = %03d" % (fitness(population[0]))) print("Execution time = %02d s" % (time.time() - start))