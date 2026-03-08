print("====================================")
print("EXAMPLE 2 : DIFFERENTIAL EVOLUTION")
print("FACTORY PRODUCTION OPTIMIZATION")
print("====================================")

# Profit values
profit = [10,8,6]

print("\nProfit per Product")
print("Product A = 10")
print("Product B = 8")
print("Product C = 6")

# ---------------------------------------
# STEP 1 : INITIAL POPULATION
# ---------------------------------------

print("\nSTEP 1 : INITIAL POPULATION")
print("------------------------------------")

P1 = [20,30,10]
P2 = [25,28,12]
P3 = [22,35,15]

plans = {"P1":P1,"P2":P2,"P3":P3} # store production plans in a dictionary for easy access

for k,v in plans.items(): # print each production plan and its product quantities
    print(k,"=",v)

# ---------------------------------------
# STEP 2 : COMPUTE PROFIT
# ---------------------------------------

print("\nSTEP 2 : COMPUTE PROFIT")
print("------------------------------------")

def compute_profit(x): # calculate total profit for a given production plan x by multiplying quantities with profit values and i-add sila
    return x[0]*10 + x[1]*8 + x[2]*6

profits = {}

for name,values in plans.items(): # calculate profit for each production plan and store in dictionary

    p = compute_profit(values) # compute profit for current plan using the compute_profit function
    profits[name] = p

    print(name)
    print(f"Profit = 10({values[0]}) + 8({values[1]}) + 6({values[2]})")
    print("Total Profit =", p)
    print()

best = max(profits, key=profits.get) # find the plan with the highest profit by using max function on profits dictionary with key=profits.get to compare values

print("Best Solution So Far =", best)
print("Maximum Profit =", profits[best])

# ---------------------------------------
# STEP 3 : MUTATION
# ---------------------------------------

print("\nSTEP 3 : MUTATION")
print("------------------------------------")

F = 0.5

print("Formula : V = P1 + F(P2 - P3)")

diff = [P2[i]-P3[i] for i in range(3)] # calculate the difference between P2 and P3 for each product by iterating through the indices and subtracting corresponding quantities

print("P2 - P3 =", diff)

scaled = [F*x for x in diff]

print("F(P2 - P3) =", scaled) # scale the difference by multiplying each element with the factor F

V = [P1[i] + scaled[i] for i in range(3)] # calculate the mutant vector V by adding the scaled difference to the original plan P1 for each product

print("Mutant Plan =", V)

# ---------------------------------------
# STEP 4 : NEW PROFIT
# ---------------------------------------

print("\nSTEP 4 : NEW PROFIT")
print("------------------------------------")

new_profit = compute_profit(V) # calculate the profit for the mutant plan V using the compute_profit function defined sa Step 2

print("Profit = 10(21.5) + 8(26.5) + 6(8.5)")
print("Total Profit =", new_profit)

if new_profit > profits[best]: 

    print("New plan is better")
    best = "Mutant"
    best_plan = V
    best_profit = new_profit

else:
    print("Previous best plan remains")
    best_plan = plans[best]
    best_profit = profits[best]
    # Keep the current best because the mutant profit is not higher.

# ---------------------------------------
# STEP 5 : FIND BEST SOLUTION
# ---------------------------------------

print("\nSTEP 5 : BEST SOLUTION")
print("------------------------------------")

print("Best Production Plan =", best_plan)
print("Profit =", best_profit)

# ---------------------------------------
# STEP 6 : FINAL RESULT
# ---------------------------------------

print("\nSTEP 6 : FINAL RESULT")
print("------------------------------------")

print("Optimal Production Plan")

print("Product A =", 22)
print("Product B =", 35)
print("Product C =", 15)

print("\nTotal Profit = 590")
print(f"The algorithm selects {best} because it produces the highest profit.")