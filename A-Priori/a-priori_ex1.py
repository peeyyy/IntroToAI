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

print("="*70)
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

# itemset formatter for consistent table output
def format_itemset(itemset):
    return "{" + ", ".join(sorted(itemset)) + "}"

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
print("-"*100)

# collect all frequent itemsets used for rules (size >= 2)
frequent_itemsets_for_rules = []

for pair, count in F2.items():
    frequent_itemsets_for_rules.append((set(pair), count))

for tri, count in F3.items():
    frequent_itemsets_for_rules.append((set(tri), count))

frequent_itemsets_for_rules = sorted(
    frequent_itemsets_for_rules,
    key=lambda x: (len(x[0]), sorted(x[0]))
)

print("We have 5 frequent itemsets:")
itemset_text = [format_itemset(itemset) for itemset, _ in frequent_itemsets_for_rules]
print("- " + ", ".join(itemset_text[:-1]) + " and " + itemset_text[-1] + ".")

print("\nTherefore, candidate rules are:")

rules=[]

for itemset, count in frequent_itemsets_for_rules:
    items = set(itemset)
    sup_count = support_count(items)
    print(f"\nFor {format_itemset(items)},")
    for i in range(1,len(items)):
        for antecedent in combinations(items,i):
            antecedent = set(antecedent)
            consequent = items-antecedent
            antecedent_count = support_count(antecedent)
            conf = support(items)/support(antecedent)
            rules.append((antecedent, consequent, conf, sup_count, antecedent_count))

            lhs = ", ".join(sorted(antecedent))
            rhs = ", ".join(sorted(consequent))
            strong_label = " (Strong)" if conf >= min_confidence else ""
            print(f"- {lhs} -> {rhs} = {sup_count}/{antecedent_count} = {conf*100:.0f}%{strong_label}")


# -----------------------------------------------------
# STRONG ASSOCIATION RULES
# -----------------------------------------------------

print("\n\nSTRONG ASSOCIATION RULES (Confidence ≥ 70%):")
print("-"*100)

for r in rules:
    antecedent, consequent, conf, sup_count, antecedent_count = r
    if conf >= min_confidence:
        print(f"{format_itemset(antecedent)} -> {format_itemset(consequent)} = {sup_count}/{antecedent_count} = {conf*100:.0f}%")

# -----------------------------------------------------
# CONCLUSION
# -----------------------------------------------------

print("\n\nCONCLUSION:")
print("-"*100)
print("A-Priori algorithm kept patterns that passed min support (30%) and min confidence (70%).")
print("{Beach, Ocean, Sunshine} was selected because it appears in 2/5 images (40% support), above 30%.")
print("Rules like {Ocean} -> {Beach, Sunshine} are strong because confidence is 100%, which is above 70%.")
print("Meaning in this dataset: example, if an image has Ocean, it also has Beach and Sunshine.")
print("-"*100)