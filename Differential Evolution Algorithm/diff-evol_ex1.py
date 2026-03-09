print("====================================")
print("EXAMPLE 1 : DIFFERENTIAL EVOLUTION")
print("CLASS SCHEDULING PROBLEM")
print("====================================")

# Preferred schedule
preferred = [9, 11, 2]

print("\nPreferred Schedule")
print("Math = 9 AM")
print("Science = 11 AM")
print("Programming = 2 PM")

# ---------------------------------------
# STEP 1 : INITIAL POPULATION
# ---------------------------------------

print("\nSTEP 1 : INITIAL POPULATION")
print("------------------------------------")

A = [8.5, 11.2, 2.1]
B = [9.3, 10.9, 2.5]
C = [8.8, 11.4, 1.8]
D = [9.1, 11.1, 2.2]

population = {"A":A, "B":B, "C":C, "D":D}

for k,v in population.items(): # print each candidate and its schedule
    print(f"{k} =", v)

# ---------------------------------------
# STEP 2 : FITNESS CALCULATION
# ---------------------------------------

print("\nSTEP 2 : FITNESS CALCULATION")
print("------------------------------------")

def fitness(x): # calculate fitness as sum of absolute differences from preferred schedule
    return abs(x[0]-9) + abs(x[1]-11) + abs(x[2]-2)
fitness_values = {}

for name,values in population.items(): # calculate fitness for each candidate and store in dictionary
    f = fitness(values)
    fitness_values[name] = f
    
    print(f"{name} Fitness =", round(f,2))

print("\nFitness Summary")
for k,v in fitness_values.items():
    print(k,"=",v)

best = min(fitness_values, key=fitness_values.get) # find candidate with lowest fitness value (best solution)

print("\nBest Candidate =", best)

# ---------------------------------------
# STEP 3 : MUTATION
# ---------------------------------------

print("\nSTEP 3 : MUTATION")
print("------------------------------------")

F = 0.5

print("Formula : V = A + F(B - C)")

BC = [B[i] - C[i] for i in range(3)] # calculate B - C for each subject

print("B - C =", BC)

scaled = [F*x for x in BC] # i-times niya sa F yung difference ng B - C

print("F(B-C) =", scaled)

V = [A[i] + scaled[i] for i in range(3)] # calculate mutant vector V by adding scaled difference to candidate A

print("Mutant Vector =", V)

# ---------------------------------------
# STEP 4 : SELECTION
# ---------------------------------------

print("\nSTEP 4 : SELECTION")
print("------------------------------------")

new_fitness = fitness(V)

print("New Candidate Fitness =", round(new_fitness,2))

print("Candidate A Fitness =", fitness_values["A"])

if new_fitness < fitness_values["A"]: # if mutant vector has better fitness than candidate A, replace A with V in population
    print("New candidate replaces Candidate A")
    population["A"] = V
else:
    print("Candidate A remains")

# ---------------------------------------
# STEP 5 : FIND BEST SOLUTION
# ---------------------------------------

print("\nSTEP 5 : FIND BEST SOLUTION")
print("------------------------------------")

best_solution = None
best_value = float("inf")

for name,values in population.items(): # calculate fitness for each candidate and find the one with the lowest fitness value (best solution)

    f = fitness(values)

    print(name,"fitness =",round(f,2))

    if f < best_value: # if current candidate has better fitness than best solution found so far, update best solution and best value
        best_value = f
        best_solution = values

print("\nBest Current Solution =", best_solution)

# ---------------------------------------
# STEP 6 : CONTINUOUS IMPROVEMENT
# ---------------------------------------

print("\nSTEP 6 : CONTINUOUS IMPROVEMENT")
print("------------------------------------")

current = best_solution

while fitness(current) > 0:

    print("Current Schedule =", current)

    # move schedule closer to preferred
    for i in range(3):

        if current[i] < preferred[i]:
            current[i] += 0.1

        elif current[i] > preferred[i]:
            current[i] -= 0.1

    current = [round(x,2) for x in current]

    print("Improved Schedule =", current)
    print("Fitness =", round(fitness(current),2))
    print()

# ---------------------------------------
# FINAL RESULT
# ---------------------------------------

print("====================================")
print("FINAL OPTIMAL SCHEDULE")
print("====================================")

print("Math =", current[0])
print("Science =", current[1])
print("Programming =", current[2])
print("Final Fitness =", fitness(current))
print("This schedule has the lowest possible fitness (0),")
print("meaning it exactly matches the preferred times with no deviation.")
print("------------------------------------")