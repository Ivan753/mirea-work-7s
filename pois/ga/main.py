import pygad
import matplotlib.pyplot as plt

from numpy import abs
from random import random

"""
Problem: approximating a parabola in the range from -5 to 5
"""


# Activation func
def re_lu(x):
    return x * (x > 0)


# Calculating NN
def nn_run(x, solution):
    hidden = [0 for _ in range(15)]

    y = 0

    for i in range(15):
        hidden[i] = re_lu(x * solution[i] + 1 * solution[30])

    for i in range(15):
        y += hidden[i] * solution[i + 15]

    return y


# Aim func
def aim_func(x):
    return x ** 2


# Fitness func for GA:
# the smaller the error, the greater the function value
def fitness_func(solution, solution_idx):
    x = random() * 4 * (-1 if random() > 0.5 else 1)
    y = nn_run(x, solution)
    error = y - aim_func(x)

    return 1.0 / abs(error)


if __name__ == "__main__":
    fitness_function = fitness_func

    num_generations = 300  # Number of generations.
    num_parents_mating = 50  # Number of solutions to be selected as parents in the mating pool.

    sol_per_pop = 150  # Number of solutions in the population.
    num_genes = 31

    init_range_low = -1
    init_range_high = 1

    parent_selection_type = "sss"  # Type of parent selection.
    keep_parents = -1  # Number of parents to keep in the next population (keep nothing)

    crossover_type = "single_point"  # Type of the crossover operator.

    # Parameters of the mutation operation.
    mutation_type = "random"  # Type of the mutation operator.
    mutation_percent_genes = 7  # Percentage of genes to mutate

    last_fitness = 0


    def callback_generation(ga_instance):
        global last_fitness
        print("Generation = {generation}, fitness = {fitness} ".format(
            generation=ga_instance.generations_completed, fitness=ga_instance.best_solution()[1]
        ))


    # Creating an instance of the GA class inside the ga module. Some parameters are initialized within the constructor.
    ga_instance = pygad.GA(
        num_generations=num_generations,
        num_parents_mating=num_parents_mating,
        fitness_func=fitness_function,
        sol_per_pop=sol_per_pop,
        num_genes=num_genes,
        init_range_low=init_range_low,
        init_range_high=init_range_high,
        parent_selection_type=parent_selection_type,
        keep_parents=keep_parents,
        crossover_type=crossover_type,
        mutation_type=mutation_type,
        mutation_percent_genes=mutation_percent_genes,
        callback_generation=callback_generation
    )

    # Running the GA to optimize the parameters of the function.
    ga_instance.run()

    # Returning the details of the best solution.
    solution, solution_fitness, solution_idx = ga_instance.best_solution()

    # Visualize the result neural network
    x = [i / 10 for i in range(-50, 50)]
    y = []

    for item in x:
        y.append(nn_run(item, solution))

    plt.plot(x, y)
    plt.show()

    # Show params
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
    print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))
