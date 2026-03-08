from itertools import combinations
from collections import Counter

# -----------------------------------------------------
# DATASET
# Each list represents tags of one image
# -----------------------------------------------------

transactions = [
    ["Beach","Sunshine","Holiday"],
    ["Sand","Beach"],
    ["Sunshine","Beach","Ocean"],
    ["Ocean","People","Beach","Sunshine"],
    ["Holiday","Sunshine"]
]

# -----------------------------------------------------
# PARAMETERS GIVEN IN THE PROBLEM
# -----------------------------------------------------

min_support_percent = 0.30      # 30%
min_confidence = 0.70           # 70%
num_transactions = len(transactions)

print("A-PRIORI ALGORITHM — IMAGE TAG MINING")
print("="*70)
print(f"Transactions: {num_transactions}")
print("Min Support: 30%")
print("Min Confidence: 70%")
print("="*70)

# -----------------------------------------------------
# DISPLAY TRANSACTIONS
# -----------------------------------------------------

print("\nTRANSACTIONS:")
print("-"*70)
print(f"{'Image ID':<15}{'Associated Tags'}")
print("-"*70)

for i,t in enumerate(transactions,1):
    print(f"{i:<15}{', '.join(t)}")

# -----------------------------------------------------
# SUPPORT FUNCTIONS
# -----------------------------------------------------

# counts how many transactions contain an itemset
def support_count(itemset):
    count=0
    for t in transactions:
        if set(itemset).issubset(t):
            count+=1
    return count

# returns support percentage
def support_percent(count):
    return (count/num_transactions)*100

# returns support value
def support(itemset):
    return support_count(itemset)/num_transactions

# -----------------------------------------------------
# FREQUENT 1-ITEMSETS
# -----------------------------------------------------

items=[]

for t in transactions:
    items.extend(t)
counter1 = Counter(items)

print("\n\nFREQUENT 1-ITEMSETS:")
print("-"*70)
print(f"{'Item':<20}{'Support':<13}{'Count'}")
print("-"*70)

F1={}

for item,count in counter1.items():
    if support_percent(count)/100 >= min_support_percent:
        F1[item]=count
        print(f"{item:<20}{support_percent(count):.0f}%{'':<10}{count}")


# -----------------------------------------------------
# FREQUENT 2-ITEMSETS
# -----------------------------------------------------

pairs=[]

for t in transactions:
    pairs.extend(combinations(sorted(t),2))
counter2 = Counter(pairs)

print("\n\nFREQUENT 2-ITEMSETS:")
print("-"*70)
print(f"{'Itemset':<30}{'Support':<13}{'Count'}")
print("-"*70)

F2={}

for pair,count in counter2.items():
    if support_percent(count)/100 >= min_support_percent:
        F2[pair]=count
        print(f"{str(pair):<30}{support_percent(count):.0f}%{'':<10}{count}")

# -----------------------------------------------------
# FREQUENT 3-ITEMSETS
# -----------------------------------------------------

triples=[]

for t in transactions:
    triples.extend(combinations(sorted(t),3))

counter3 = Counter(triples)

print("\n\nFREQUENT 3-ITEMSETS:")
print("-"*70)
print(f"{'Itemset':<35}{'Support':<13}{'Count'}")
print("-"*70)

F3={}

for tri,count in counter3.items():
    if support_percent(count)/100 >= min_support_percent:
        F3[tri]=count
        print(f"{str(tri):<35}{support_percent(count):.0f}%{'':<10}{count}")


# -----------------------------------------------------
# ASSOCIATION RULES
# -----------------------------------------------------

print("\n\nASSOCIATION RULES:")
print("-"*116)

row_fmt = "{:<28}{:<4}{:<28}{:>10}{:>8}{:>12}{:>8}"

print(row_fmt.format("Antecedent","->","Consequent","Support","Count","Confidence","Lift"))
print("-"*116)

rules=[]

for tri,count in F3.items():

    items=set(tri)
    for i in range(1,len(items)):
        for antecedent in combinations(items,i):
            antecedent=set(antecedent)
            consequent=items-antecedent
            conf = support(items)/support(antecedent)
            lift = conf/support(consequent)
            sup_count=support_count(items)
            rules.append((antecedent,consequent,conf,lift,sup_count))

            print(row_fmt.format(
                str(antecedent),
                "->",
                str(consequent),
                f"{support_percent(sup_count):.0f}%",
                sup_count,
                f"{conf*100:.0f}%",
                f"{lift:.2f}"
            ))


# -----------------------------------------------------
# STRONG ASSOCIATION RULES
# -----------------------------------------------------

print("\n\nSTRONG ASSOCIATION RULES (Confidence ≥ 70%):")
print("- For {Beach, Ocean, Sunshine}, the following strong rules were found:")
print("-"*100)

for r in rules:
    antecedent,consequent,conf,lift,count=r
    if conf >= min_confidence:
        print(f"{antecedent} -> {consequent}  (Confidence = {conf*100:.0f}%)")

# -----------------------------------------------------
# CONCLUSION
# -----------------------------------------------------

print("\n\nCONCLUSION:")
print("-"*100)
print("The A-Priori algorithm discovered patterns among image tags.")
print("The rules with confidence greater than or equal to 70% are considered strong rules.")
print("These rules indicate that when certain tags appear in an image, other tags are very likely to appear with them.")
print("For example, tags such as Ocean, Beach, and Sunshine often occur together in the dataset.")
print("-"*100)